import datetime
from functools import partial
from django.conf import settings
from django.db import models

from karrio.server.core.utils import identity
from karrio.server.core.models import OwnedEntity, uuid
from karrio.server.manager import models as manager

from karrio.server.orders.serializers.base import ORDER_STATUS


class LineItem(manager.Commodity):
    class Meta:
        proxy = True

    @property
    def unfulfilled_quantity(self):
        quantity = self.quantity - sum(
            [
                child.quantity or 0
                for child in list(
                    self.children.exclude(
                        commodity_parcel__parcel_shipment__status__in=[
                            "cancelled",
                            "draft",
                        ]
                    ).filter(
                        commodity_parcel__isnull=False,
                        commodity_customs__isnull=True,
                    )
                )
            ],
            0,
        )
        return quantity if quantity > 0 else 0


class OrderManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "shipping_to",
                "shipping_from",
                "line_items",
                "line_items__children__commodity_parcel__parcel_shipment",
            )
        )


class Order(OwnedEntity):
    HIDDEN_PROPS = (*(("org",) if settings.MULTI_ORGANIZATIONS else tuple()),)
    DIRECT_PROPS = [
        "order_id",
        "order_date",
        "source",
        "status",
        "options",
        "metadata",
        "test_mode",
        "created_by",
    ]
    objects = OrderManager()

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]

    id = models.CharField(
        max_length=50,
        primary_key=True,
        default=partial(uuid, prefix="ord_"),
        editable=False,
    )
    order_id = models.CharField(max_length=50)
    order_date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(
        max_length=25, choices=ORDER_STATUS, default=ORDER_STATUS[0][0]
    )
    shipping_to = models.OneToOneField(
        "manager.Address", on_delete=models.CASCADE, related_name="recipient_order"
    )
    shipping_from = models.OneToOneField(
        "manager.Address",
        null=True,
        on_delete=models.CASCADE,
        related_name="shipper_order",
    )
    line_items = models.ManyToManyField(
        LineItem, related_name="commodity_order", through="OrderLineItemLink"
    )
    options = models.JSONField(
        blank=True, null=True, default=partial(identity, value={})
    )
    test_mode = models.BooleanField()
    metadata = models.JSONField(
        blank=True, null=True, default=partial(identity, value={})
    )

    @property
    def object_type(self):
        return "order"

    # computed fields

    @property
    def shipments(self):
        return manager.Shipment.objects.filter(
            parcels__items__parent_id__in=self.line_items.values_list("id", flat=True)
        ).distinct()


"""Models orders linking (for reverse OneToMany relations)"""


class OrderLineItemLink(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="line_item_links"
    )
    item = models.OneToOneField(
        LineItem, on_delete=models.CASCADE, related_name="order_link"
    )