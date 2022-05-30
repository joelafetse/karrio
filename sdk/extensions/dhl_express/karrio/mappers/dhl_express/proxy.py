from typing import Any
from karrio.core.utils import DP, request as http, Serializable, Deserializable
from karrio.api.proxy import Proxy as BaseProxy
from dhl_express_lib.dct_req_global_2_0 import DCTRequest
from dhl_express_lib.tracking_request_known_1_0 import KnownTrackingRequest
from dhl_express_lib.ship_val_global_req_10_0 import ShipmentRequest
from dhl_express_lib.book_pickup_global_req_3_0 import BookPURequest
from dhl_express_lib.modify_pickup_global_req_3_0 import ModifyPURequest
from dhl_express_lib.cancel_pickup_global_req_3_0 import CancelPURequest
from dhl_express_lib.routing_global_req_2_0 import RouteRequest
from karrio.mappers.dhl_express.settings import Settings


class Proxy(BaseProxy):
    settings: Settings

    def _send_request(
        self, path: str, request: Serializable = None, method: str = "POST"
    ) -> str:
        data: dict = (
            dict(data=bytearray(request.serialize(), "utf-8"))
            if request is not None
            else dict()
        )
        return http(
            **{
                "url": f"{self.settings.server_url}{path}",
                "headers": {"Content-Type": "application/json"},
                "method": method,
                **data,
            }
        )

    def validate_address(self, request: Serializable) -> Deserializable[str]:
        response = self._send_request(
            path="/address-validate",
            request=Serializable(request, DP.jsonify),
            method="GET",
        )

        return Deserializable(response, DP.to_dict)

    def get_rates(self, request: Serializable) -> Deserializable[str]:
        response = self._send_request(
            path="/rates", request=Serializable(request, DP.jsonify)
        )

        return Deserializable(response, DP.to_dict)

    # def get_tracking(
    #     self, request: Serializable[KnownTrackingRequest]
    # ) -> Deserializable[str]:
    #     response = self._send_request(request)

    #     return Deserializable(response, XP.to_xml)

    # def create_shipment(
    #     self, request: Serializable[ShipmentRequest]
    # ) -> Deserializable[str]:
    #     response = self._send_request(request)

    #     return Deserializable(response, XP.to_xml)

    # def schedule_pickup(
    #     self, request: Serializable[BookPURequest]
    # ) -> Deserializable[str]:
    #     response = self._send_request(request)

    #     return Deserializable(response, XP.to_xml)

    # def modify_pickup(
    #     self, request: Serializable[ModifyPURequest]
    # ) -> Deserializable[str]:
    #     response = self._send_request(request)

    #     return Deserializable(response, XP.to_xml)

    # def cancel_pickup(
    #     self, request: Serializable[CancelPURequest]
    # ) -> Deserializable[str]:
    #     response = self._send_request(request)

    #     return Deserializable(response, XP.to_xml)
