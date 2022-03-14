import logging
from django.db.models import signals

from purplship.server.core import utils
from purplship.server import serializers
import purplship.server.documents.models as models

logger = logging.getLogger(__name__)


def register_all():
    signals.post_save.connect(document_updated, sender=models.DocumentTemplate)

    logger.info("documents webhooks signals registered...")


@utils.disable_for_loaddata
def document_updated(sender, instance, *args, **kwargs):
    changes = kwargs.get("update_fields") or []

    if "created_at" in changes:
        duplicates = models.DocumentTemplate.objects.filter(
            slug=instance.slug,
            org=instance.link.org,
        ).count()

        if duplicates > 1:
            raise serializers.ValidationError(
                {"slug": "Document template with this slug already exists."}
            )