from typing import Tuple, List
from karrio.core.utils import Serializable, DP
from karrio.core.models import (
    AddressValidationRequest,
    Message,
    AddressValidationDetails,
)
from karrio.providers.dhl_express.utils import Settings
from karrio.providers.dhl_express.error import parse_error_response
from schemas.dhl_express.dhl_express_lib.validate_address_response import (
    ValidateAddressResponse,
)
from schemas.dhl_express.dhl_express_lib.validate_address_request import (
    ValidateAddressRequest,
)


def parse_address_validation_response(
    response: ValidateAddressResponse, settings: Settings
) -> Tuple[AddressValidationDetails, List[Message]]:
    success = True if "address" in response else False
    validation_details = AddressValidationDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        success=success,
    )

    return validation_details, parse_error_response(response, settings)


def address_validation_request(
    payload: AddressValidationRequest, settings: Settings
) -> Serializable[ValidateAddressRequest]:

    request = ValidateAddressRequest(
        type=payload.address.extra.type,
        countryCode=payload.address.country_code,
        postalCode=payload.address.postal_code,
        cityName=payload.address.city,
        strictValidation=payload.address.extra.strict_validation,
    )

    return Serializable(request, DP.to_dict, logged=True)
