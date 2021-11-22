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


class ProvisionAdvanceParameters(object):
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
        'connection_initiator': 'str',
        'tag': 'str',
        'server_host_name': 'str',
        'server_port': 'int'
    }

    attribute_map = {
        'connection_initiator': 'connectionInitiator',
        'tag': 'tag',
        'server_host_name': 'serverHostName',
        'server_port': 'serverPort'
    }

    def __init__(self, connection_initiator=None, tag=None, server_host_name=None, server_port=None, _configuration=None):  # noqa: E501
        """ProvisionAdvanceParameters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_initiator = None
        self._tag = None
        self._server_host_name = None
        self._server_port = None
        self.discriminator = None

        if connection_initiator is not None:
            self.connection_initiator = connection_initiator
        if tag is not None:
            self.tag = tag
        if server_host_name is not None:
            self.server_host_name = server_host_name
        if server_port is not None:
            self.server_port = server_port

    @property
    def connection_initiator(self):
        """Gets the connection_initiator of this ProvisionAdvanceParameters.  # noqa: E501

        Which component is allowed to initiate the connection [ServerToAgent | AgentToServer | BothAllowed]. Parameters start with capital letter.  HIDDEN.  # noqa: E501

        :return: The connection_initiator of this ProvisionAdvanceParameters.  # noqa: E501
        :rtype: str
        """
        return self._connection_initiator

    @connection_initiator.setter
    def connection_initiator(self, connection_initiator):
        """Sets the connection_initiator of this ProvisionAdvanceParameters.

        Which component is allowed to initiate the connection [ServerToAgent | AgentToServer | BothAllowed]. Parameters start with capital letter.  HIDDEN.  # noqa: E501

        :param connection_initiator: The connection_initiator of this ProvisionAdvanceParameters.  # noqa: E501
        :type: str
        """

        self._connection_initiator = connection_initiator

    @property
    def tag(self):
        """Gets the tag of this ProvisionAdvanceParameters.  # noqa: E501

        Logical name that is used to label specific Control-M/Agents into a group with a specific authorization level.  HIDDEN.  # noqa: E501

        :return: The tag of this ProvisionAdvanceParameters.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ProvisionAdvanceParameters.

        Logical name that is used to label specific Control-M/Agents into a group with a specific authorization level.  HIDDEN.  # noqa: E501

        :param tag: The tag of this ProvisionAdvanceParameters.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def server_host_name(self):
        """Gets the server_host_name of this ProvisionAdvanceParameters.  # noqa: E501

        Control-M/Server name (in case it has an alias or multiple network interfaces).  HIDDEN.  # noqa: E501

        :return: The server_host_name of this ProvisionAdvanceParameters.  # noqa: E501
        :rtype: str
        """
        return self._server_host_name

    @server_host_name.setter
    def server_host_name(self, server_host_name):
        """Sets the server_host_name of this ProvisionAdvanceParameters.

        Control-M/Server name (in case it has an alias or multiple network interfaces).  HIDDEN.  # noqa: E501

        :param server_host_name: The server_host_name of this ProvisionAdvanceParameters.  # noqa: E501
        :type: str
        """

        self._server_host_name = server_host_name

    @property
    def server_port(self):
        """Gets the server_port of this ProvisionAdvanceParameters.  # noqa: E501

        Control-M/Server port to communicate with the agent.  HIDDEN.  # noqa: E501

        :return: The server_port of this ProvisionAdvanceParameters.  # noqa: E501
        :rtype: int
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        """Sets the server_port of this ProvisionAdvanceParameters.

        Control-M/Server port to communicate with the agent.  HIDDEN.  # noqa: E501

        :param server_port: The server_port of this ProvisionAdvanceParameters.  # noqa: E501
        :type: int
        """

        self._server_port = server_port

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
        if issubclass(ProvisionAdvanceParameters, dict):
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
        if not isinstance(other, ProvisionAdvanceParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvisionAdvanceParameters):
            return True

        return self.to_dict() != other.to_dict()
