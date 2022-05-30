import time
from typing import List, Tuple, cast, Iterable
from schemas.dhl_express.dhl_express_lib.rating_response import RatingResponse
from dhl_express_lib.dct_req_global_2_0 import (
    DCTRequest,
    DCTTo,
    DCTFrom,
    GetQuoteType,
    BkgDetailsType,
    PiecesType,
    MetaData,
    PieceType,
    QtdShpType,
    QtdShpExChrgType,
)
from dhl_express_lib.dct_requestdatatypes_global import DCTDutiable
from dhl_express_lib.dct_response_global_2_0 import QtdShpType as ResponseQtdShpType

from karrio.core.errors import DestinationNotServicedError, OriginNotServicedError
from karrio.core.utils import Serializable, NF, XP, DF, DP
from karrio.core.units import Packages, Options, Package, Services, CountryCurrency
from karrio.core.models import RateDetails, Message, ChargeDetails, RateRequest
from karrio.providers.dhl_express.units import (
    ProductCode,
    DCTPackageType,
    PackagePresets,
    SpecialServiceCode,
    NetworkType,
    COUNTRY_PREFERED_UNITS,
    MeasurementOptions,
)
from karrio.providers.dhl_express.utils import Settings
from karrio.providers.dhl_express.error import parse_error_response
from schemas.dhl_express.dhl_express_lib.rating_response import RatingResponse, Product
import schemas.dhl_express.dhl_express_lib.rating_request as dhlExpress


def parse_rate_response(
    response: dict, settings: Settings
) -> Tuple[List[RateDetails], List[Message]]:

    rates: List[RateDetails] = [
        _extract_product(data, settings) for data in response.get("products", [])
    ]

    return rates, parse_error_response(response, settings)


def _extract_product(data: dict, settings: Settings) -> RateDetails:
    product = DP.to_object(Product, data)
    service = ProductCode.map(product.productCode)
    # charges = [
    #     ("Base charge", quote.WeightCharge),
    #     *((s.LocalServiceTypeName, s.ChargeValue) for s in quote.QtdShpExChrg),
    # ]

    delivery_date = DF.date(
        product.deliveryCapabilities.estimatedDeliveryDateAndTime, "%Y-%m-%d %H:%M:%S"
    )
    pricing_date = DF.date(product.pricingDate)
    transit = (
        (delivery_date.date() - pricing_date.date()).days
        if all([delivery_date, pricing_date])
        else None
    )

    return RateDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        # currency=quote.CurrencyCode,
        transit_days=transit,
        service=service.name_or_key,
        # total_charge=NF.decimal(quote.ShippingCharge),
        # extra_charges=[
        #     ChargeDetails(
        #         name=name,
        #         amount=NF.decimal(amount),
        #         currency=quote.CurrencyCode,
        #     )
        #     for name, amount in charges
        #     if amount
        # ],
        meta=dict(service_name=(service.name or product.productName)),
    )


def rate_request(payload: RateRequest, settings: Settings) -> Serializable:
    packages = Packages(payload.parcels, PackagePresets, required=["weight"])
    products = [*Services(payload.services, ProductCode)]
    options = Options(payload.options, SpecialServiceCode)

    is_international = payload.shipper.country_code != payload.recipient.country_code

    if any(settings.account_country_code or "") and (
        payload.shipper.country_code != settings.account_country_code
    ):
        raise OriginNotServicedError(payload.shipper.country_code)
    if not is_international and payload.shipper.country_code in ["CA"]:
        raise DestinationNotServicedError(payload.shipper.country_code)

    is_document = all([parcel.is_document for parcel in payload.parcels])
    is_dutiable = not is_document
    weight_unit, dim_unit = (
        COUNTRY_PREFERED_UNITS.get(payload.shipper.country_code)
        or packages.compatible_units
    )
    paperless = (
        SpecialServiceCode.dhl_paperless_trade
        if (is_international and is_dutiable)
        else None
    )
    special_services = [
        *options,
        *([(paperless.name, None)] if paperless is not None else []),
    ]
    insurance = (
        options["dhl_shipment_insurance"].value
        if "dhl_shipment_insurance" in options
        else None
    )

    if len(products) == 0:
        if is_international and is_document:
            product = "dhl_express_worldwide_doc"
        elif is_international:
            product = "dhl_express_worldwide_nondoc"
        elif is_document and "envelope" in packages[0].packaging_type:
            product = "dhl_express_envelope_doc"
        elif is_document:
            product = "dhl_domestic_express_doc"
        else:
            product = "dhl_express_12_00_nondoc"

        products = [ProductCode[product]]

    request = DCTRequest(
        GetQuote=GetQuoteType(
            Request=settings.Request(
                MetaData=MetaData(SoftwareName="3PV", SoftwareVersion=1.0)
            ),
            From=DCTFrom(
                CountryCode=payload.shipper.country_code,
                Postalcode=payload.shipper.postal_code,
                City=payload.shipper.city,
                Suburb=payload.shipper.state_code,
            ),
            To=DCTTo(
                CountryCode=payload.recipient.country_code,
                Postalcode=payload.recipient.postal_code,
                City=payload.recipient.city,
                Suburb=payload.recipient.state_code,
            ),
            BkgDetails=BkgDetailsType(
                PaymentCountryCode=payload.shipper.country_code,
                NetworkTypeCode=NetworkType.both_time_and_day_definite.value,
                WeightUnit=weight_unit.value,
                DimensionUnit=dim_unit.value,
                ReadyTime=time.strftime("PT%HH%MM"),
                Date=time.strftime("%Y-%m-%d"),
                IsDutiable=("Y" if is_dutiable else "N"),
                Pieces=PiecesType(
                    Piece=[
                        PieceType(
                            PieceID=package.parcel.id or f"{index}",
                            PackageTypeCode=DCTPackageType[
                                package.packaging_type or "your_packaging"
                            ].value,
                            Depth=package.length.map(MeasurementOptions)[dim_unit.name],
                            Width=package.width.map(MeasurementOptions)[dim_unit.name],
                            Height=package.height.map(MeasurementOptions)[
                                dim_unit.name
                            ],
                            Weight=package.weight[weight_unit.name],
                        )
                        for index, package in enumerate(
                            cast(Iterable[Package], packages), 1
                        )
                    ]
                ),
                NumberOfPieces=len(packages),
                ShipmentWeight=packages.weight[weight_unit.name],
                Volume=None,
                PaymentAccountNumber=settings.account_number,
                InsuredCurrency=(options.currency if insurance is not None else None),
                InsuredValue=insurance,
                PaymentType=None,
                AcctPickupCloseTime=None,
                QtdShp=[
                    QtdShpType(
                        GlobalProductCode=product.value,
                        LocalProductCode=product.value,
                        QtdShpExChrg=[
                            QtdShpExChrgType(
                                SpecialServiceType=SpecialServiceCode[key].value.key
                            )
                            for key, _ in special_services
                            if key in SpecialServiceCode
                        ],
                    )
                    for product in products
                ],
            ),
            Dutiable=(
                DCTDutiable(
                    DeclaredValue=(insurance or 1.0),
                    DeclaredCurrency=(
                        options.currency
                        or CountryCurrency[payload.shipper.country_code].value
                    ),
                )
                if is_dutiable
                else None
            ),
        ),
    )

    request = dhlExpress.RatingRequest(
        customerDetails=dhlExpress.CustomerDetails(
            shipperDetails=dhlExpress.ErDetails(
                postalCode=payload.shipper.postal_code,
                cityName=payload.shipper.city,
                countryCode=payload.shipper.country_code,
                addressLine1=payload.shipper.address_line1,
                addressLine2=payload.shipper.address_line2,
            ),
            receiverDetails=dhlExpress.ErDetails(
                postalCode=payload.recipient.postal_code,
                cityName=payload.recipient.city,
                countryCode=payload.recipient.country_code,
                addressLine1=payload.recipient.address_line1,
                addressLine2=payload.recipient.address_line2,
            ),
        ),
        productCode=payload,
    )

    return Serializable(request, DP.to_dict, logged=True)
