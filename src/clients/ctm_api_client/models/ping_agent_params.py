# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.215
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clients.ctm_api_client.configuration import Configuration


class PingAgentParams(object):
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
    swagger_types = {"discover": "bool", "timeout": "int"}

    attribute_map = {"discover": "discover", "timeout": "timeout"}

    def __init__(self, discover=False, timeout=60, _configuration=None):  # noqa: E501
        """PingAgentParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._discover = None
        self._timeout = None
        self.discriminator = None

        self.discover = discover
        self.timeout = timeout

    @property
    def discover(self):
        """Gets the discover of this PingAgentParams.  # noqa: E501

        Discover parameter when true the agent will be added to the Control-M. HIDDEN  # noqa: E501

        :return: The discover of this PingAgentParams.  # noqa: E501
        :rtype: bool
        """
        return self._discover

    @discover.setter
    def discover(self, discover):
        """Sets the discover of this PingAgentParams.

        Discover parameter when true the agent will be added to the Control-M. HIDDEN  # noqa: E501

        :param discover: The discover of this PingAgentParams.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and discover is None:
            raise ValueError(
                "Invalid value for `discover`, must not be `None`"
            )  # noqa: E501

        self._discover = discover

    @property
    def timeout(self):
        """Gets the timeout of this PingAgentParams.  # noqa: E501

        maximum time in seconds to wait (default 60). HIDDEN  # noqa: E501

        :return: The timeout of this PingAgentParams.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this PingAgentParams.

        maximum time in seconds to wait (default 60). HIDDEN  # noqa: E501

        :param timeout: The timeout of this PingAgentParams.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and timeout is None:
            raise ValueError(
                "Invalid value for `timeout`, must not be `None`"
            )  # noqa: E501

        self._timeout = timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(PingAgentParams, dict):
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
        if not isinstance(other, PingAgentParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PingAgentParams):
            return True

        return self.to_dict() != other.to_dict()
