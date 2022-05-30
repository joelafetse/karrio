from typing import List
from karrio.providers.dhl_express import Settings
from karrio.core.models import Message
from karrio.core.utils import DP
from schemas.dhl_express.dhl_express_lib.error import Error


def parse_error_response(
    response: dict, settings: Settings, details: dict = None
) -> List[Message]:
    errors = DP.to_object(Error, response)

    return [
        Message(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            code=error.code,
            message=error.title,
            details={
                **(details or {}),
                **({} if error.detail is None else {"note": error.detail}),
            },
        )
        for error in errors.invalidParameters
    ]
