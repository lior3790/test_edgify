# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.order_info import OrderInfo  # noqa: F401,E501
from swagger_server import util


class SingleOrder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, order_info: OrderInfo=None):  # noqa: E501
        """SingleOrder - a model defined in Swagger

        :param id: The id of this SingleOrder.  # noqa: E501
        :type id: str
        :param order_info: The order_info of this SingleOrder.  # noqa: E501
        :type order_info: OrderInfo
        """
        self.swagger_types = {
            'id': str,
            'order_info': OrderInfo
        }

        self.attribute_map = {
            'id': 'id',
            'order_info': 'orderInfo'
        }
        self._id = id
        self._order_info = order_info

    @classmethod
    def from_dict(cls, dikt) -> 'SingleOrder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SingleOrder of this SingleOrder.  # noqa: E501
        :rtype: SingleOrder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SingleOrder.


        :return: The id of this SingleOrder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SingleOrder.


        :param id: The id of this SingleOrder.
        :type id: str
        """

        self._id = id

    @property
    def order_info(self) -> OrderInfo:
        """Gets the order_info of this SingleOrder.


        :return: The order_info of this SingleOrder.
        :rtype: OrderInfo
        """
        return self._order_info

    @order_info.setter
    def order_info(self, order_info: OrderInfo):
        """Sets the order_info of this SingleOrder.


        :param order_info: The order_info of this SingleOrder.
        :type order_info: OrderInfo
        """

        self._order_info = order_info
