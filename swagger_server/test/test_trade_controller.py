# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.single_order import SingleOrder  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTradeController(BaseTestCase):
    """TradeController integration test stubs"""

    def test_trade_csv(self):
        """Test case for trade_csv

        Upload trade orders
        """
        data = dict(csv_file='csv_file_example')
        response = self.client.open(
            '/v2/trade',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
