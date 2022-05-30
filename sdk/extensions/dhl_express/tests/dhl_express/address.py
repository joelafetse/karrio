import re
import unittest
import logging
from unittest.mock import patch
import karrio
from karrio.core.utils import DP
from karrio.core.models import AddressValidationRequest
from tests.dhl_express.fixture import gateway


class TestDHLAddressValidation(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.AddressValidationRequest = AddressValidationRequest(
            **address_validation_data
        )

    def test_create_AddressValidation_request(self):
        request = gateway.mapper.create_address_validation_request(
            self.AddressValidationRequest
        )

        self.assertEqual(request.serialize(), AddressValidationRequestJson)

    def test_validate_address(self):
        with patch("karrio.mappers.dhl_express.proxy.http") as mock:
            mock.return_value = "{}"
            karrio.Address.validate(self.AddressValidationRequest).from_(gateway)
            self.assertEqual(
                mock.call_args[1]["url"],
                gateway.settings.server_url + "/address-validate",
            )

    def test_parse_address_validation_response(self):
        with patch("karrio.mappers.dhl_express.proxy.http") as mock:
            mock.return_value = AddressValidationResponseJson
            parsed_response = (
                karrio.Address.validate(self.AddressValidationRequest)
                .from_(gateway)
                .parse()
            )

            self.assertEqual(
                DP.to_dict(parsed_response), DP.to_dict(ParsedAddressValidationResponse)
            )


if __name__ == "__main__":
    unittest.main()

address_validation_data = {
    "address": {
        "postal_code": "14800",
        "city": "Prague",
        "country_code": "CZ",
        "extra": {"type": "pickup", "strict_validation": True},
    }
}

ParsedAddressValidationResponse = [
    {
        "carrier_id": "carrier_id",
        "carrier_name": "dhl_express",
        "success": True,
    },
    [],
]


AddressValidationRequestJson = {
    "type": "pickup",
    "countryCode": "CZ",
    "postalCode": "14800",
    "cityName": "Prague",
    "strictValidation": True,
}


AddressValidationResponseJson = """{
  "warnings": [
    "warning 1"
  ],
  "address": [
    {
      "countryCode": "CZ",
      "postalCode": "14800",
      "cityName": "PRAGUE",
      "countyName": "PRAGUE-CZECH REPUBLIC",
      "serviceArea": {
        "code": "PRG",
        "description": "PRAGUE-CZECH REPUBLIC, THE",
        "GMTOffset": "+01:00"
      }
    }
  ]
}
"""
