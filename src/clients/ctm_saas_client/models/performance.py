# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.30
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clients.ctm_saas_client.configuration import Configuration


class Performance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'name': 'str',
        'unit': 'str',
        'value': 'str',
        'key': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'unit': 'unit',
        'value': 'value',
        'key': 'key'
    }

    def __init__(self, type=None, name=None, unit=None, value=None, key=None, _configuration=None):  # noqa: E501
        """Performance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._name = None
        self._unit = None
        self._value = None
        self._key = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if key is not None:
            self.key = key

    @property
    def type(self):
        """Gets the type of this Performance.  # noqa: E501

        the type of the availability metric  # noqa: E501

        :return: The type of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Performance.

        the type of the availability metric  # noqa: E501

        :param type: The type of this Performance.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Performance.  # noqa: E501

        the name of the metric  # noqa: E501

        :return: The name of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Performance.

        the name of the metric  # noqa: E501

        :param name: The name of this Performance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this Performance.  # noqa: E501

        the unit of measurement  # noqa: E501

        :return: The unit of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Performance.

        the unit of measurement  # noqa: E501

        :param unit: The unit of this Performance.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this Performance.  # noqa: E501

        the value of the metric  # noqa: E501

        :return: The value of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Performance.

        the value of the metric  # noqa: E501

        :param value: The value of this Performance.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def key(self):
        """Gets the key of this Performance.  # noqa: E501

        A unique key for the metric  # noqa: E501

        :return: The key of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Performance.

        A unique key for the metric  # noqa: E501

        :param key: The key of this Performance.  # noqa: E501
        :type: str
        """

        self._key = key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Performance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Performance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Performance):
            return True

        return self.to_dict() != other.to_dict()
