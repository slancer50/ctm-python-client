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


class LdapDomainSettings(object):
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
        "domain_name": "str",
        "directory_search_user": "str",
        "directory_search_password": "str",
        "communication_protocol": "str",
        "directory_server_type": "str",
        "server_host_name_and_port": "list[HostnamePortPair]",
        "directory_search_base": "list[str]",
    }

    attribute_map = {
        "domain_name": "domainName",
        "directory_search_user": "directorySearchUser",
        "directory_search_password": "directorySearchPassword",
        "communication_protocol": "communicationProtocol",
        "directory_server_type": "directoryServerType",
        "server_host_name_and_port": "serverHostNameAndPort",
        "directory_search_base": "directorySearchBase",
    }

    def __init__(
        self,
        domain_name=None,
        directory_search_user=None,
        directory_search_password=None,
        communication_protocol=None,
        directory_server_type=None,
        server_host_name_and_port=None,
        directory_search_base=None,
        _configuration=None,
    ):  # noqa: E501
        """LdapDomainSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain_name = None
        self._directory_search_user = None
        self._directory_search_password = None
        self._communication_protocol = None
        self._directory_server_type = None
        self._server_host_name_and_port = None
        self._directory_search_base = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if directory_search_user is not None:
            self.directory_search_user = directory_search_user
        if directory_search_password is not None:
            self.directory_search_password = directory_search_password
        if communication_protocol is not None:
            self.communication_protocol = communication_protocol
        if directory_server_type is not None:
            self.directory_server_type = directory_server_type
        if server_host_name_and_port is not None:
            self.server_host_name_and_port = server_host_name_and_port
        if directory_search_base is not None:
            self.directory_search_base = directory_search_base

    @property
    def domain_name(self):
        """Gets the domain_name of this LdapDomainSettings.  # noqa: E501


        :return: The domain_name of this LdapDomainSettings.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this LdapDomainSettings.


        :param domain_name: The domain_name of this LdapDomainSettings.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def directory_search_user(self):
        """Gets the directory_search_user of this LdapDomainSettings.  # noqa: E501


        :return: The directory_search_user of this LdapDomainSettings.  # noqa: E501
        :rtype: str
        """
        return self._directory_search_user

    @directory_search_user.setter
    def directory_search_user(self, directory_search_user):
        """Sets the directory_search_user of this LdapDomainSettings.


        :param directory_search_user: The directory_search_user of this LdapDomainSettings.  # noqa: E501
        :type: str
        """

        self._directory_search_user = directory_search_user

    @property
    def directory_search_password(self):
        """Gets the directory_search_password of this LdapDomainSettings.  # noqa: E501


        :return: The directory_search_password of this LdapDomainSettings.  # noqa: E501
        :rtype: str
        """
        return self._directory_search_password

    @directory_search_password.setter
    def directory_search_password(self, directory_search_password):
        """Sets the directory_search_password of this LdapDomainSettings.


        :param directory_search_password: The directory_search_password of this LdapDomainSettings.  # noqa: E501
        :type: str
        """

        self._directory_search_password = directory_search_password

    @property
    def communication_protocol(self):
        """Gets the communication_protocol of this LdapDomainSettings.  # noqa: E501


        :return: The communication_protocol of this LdapDomainSettings.  # noqa: E501
        :rtype: str
        """
        return self._communication_protocol

    @communication_protocol.setter
    def communication_protocol(self, communication_protocol):
        """Sets the communication_protocol of this LdapDomainSettings.


        :param communication_protocol: The communication_protocol of this LdapDomainSettings.  # noqa: E501
        :type: str
        """

        self._communication_protocol = communication_protocol

    @property
    def directory_server_type(self):
        """Gets the directory_server_type of this LdapDomainSettings.  # noqa: E501


        :return: The directory_server_type of this LdapDomainSettings.  # noqa: E501
        :rtype: str
        """
        return self._directory_server_type

    @directory_server_type.setter
    def directory_server_type(self, directory_server_type):
        """Sets the directory_server_type of this LdapDomainSettings.


        :param directory_server_type: The directory_server_type of this LdapDomainSettings.  # noqa: E501
        :type: str
        """

        self._directory_server_type = directory_server_type

    @property
    def server_host_name_and_port(self):
        """Gets the server_host_name_and_port of this LdapDomainSettings.  # noqa: E501


        :return: The server_host_name_and_port of this LdapDomainSettings.  # noqa: E501
        :rtype: list[HostnamePortPair]
        """
        return self._server_host_name_and_port

    @server_host_name_and_port.setter
    def server_host_name_and_port(self, server_host_name_and_port):
        """Sets the server_host_name_and_port of this LdapDomainSettings.


        :param server_host_name_and_port: The server_host_name_and_port of this LdapDomainSettings.  # noqa: E501
        :type: list[HostnamePortPair]
        """

        self._server_host_name_and_port = server_host_name_and_port

    @property
    def directory_search_base(self):
        """Gets the directory_search_base of this LdapDomainSettings.  # noqa: E501


        :return: The directory_search_base of this LdapDomainSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._directory_search_base

    @directory_search_base.setter
    def directory_search_base(self, directory_search_base):
        """Sets the directory_search_base of this LdapDomainSettings.


        :param directory_search_base: The directory_search_base of this LdapDomainSettings.  # noqa: E501
        :type: list[str]
        """

        self._directory_search_base = directory_search_base

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
        if issubclass(LdapDomainSettings, dict):
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
        if not isinstance(other, LdapDomainSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LdapDomainSettings):
            return True

        return self.to_dict() != other.to_dict()
