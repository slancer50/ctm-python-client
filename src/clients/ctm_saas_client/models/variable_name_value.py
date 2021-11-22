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


class VariableNameValue(object):
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
        'variable_name': 'str',
        'variable_value': 'str'
    }

    attribute_map = {
        'variable_name': 'variable_name',
        'variable_value': 'variable_value'
    }

    def __init__(self, variable_name=None, variable_value=None, _configuration=None):  # noqa: E501
        """VariableNameValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._variable_name = None
        self._variable_value = None
        self.discriminator = None

        if variable_name is not None:
            self.variable_name = variable_name
        if variable_value is not None:
            self.variable_value = variable_value

    @property
    def variable_name(self):
        """Gets the variable_name of this VariableNameValue.  # noqa: E501


        :return: The variable_name of this VariableNameValue.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this VariableNameValue.


        :param variable_name: The variable_name of this VariableNameValue.  # noqa: E501
        :type: str
        """

        self._variable_name = variable_name

    @property
    def variable_value(self):
        """Gets the variable_value of this VariableNameValue.  # noqa: E501


        :return: The variable_value of this VariableNameValue.  # noqa: E501
        :rtype: str
        """
        return self._variable_value

    @variable_value.setter
    def variable_value(self, variable_value):
        """Sets the variable_value of this VariableNameValue.


        :param variable_value: The variable_value of this VariableNameValue.  # noqa: E501
        :type: str
        """

        self._variable_value = variable_value

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
        if issubclass(VariableNameValue, dict):
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
        if not isinstance(other, VariableNameValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VariableNameValue):
            return True

        return self.to_dict() != other.to_dict()
