import unittest

from flask import json

from openapi_server.models.callbacks_post201_response import CallbacksPost201Response  # noqa: E501
from openapi_server.models.healthcheck_get200_response import HealthcheckGet200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_callbacks_post(self):
        """Test case for callbacks_post

        
        """
        query_string = [('callbackUrl', 'http://server/foo/bar')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/callbacks',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_healthcheck_get(self):
        """Test case for healthcheck_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/healthcheck',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
