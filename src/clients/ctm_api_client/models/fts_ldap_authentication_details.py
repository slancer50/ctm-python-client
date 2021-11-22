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


class FtsLdapAuthenticationDetails(object):
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
        "search_user_name": "str",
        "search_user_password": "str",
        "server_url": "str",
        "base_dn": "str",
        "username_attribute_name": "str",
        "dn_attribute_name": "str",
        "connection_timeout": "int",
    }

    attribute_map = {
        "search_user_name": "searchUserName",
        "search_user_password": "searchUserPassword",
        "server_url": "serverUrl",
        "base_dn": "baseDn",
        "username_attribute_name": "usernameAttributeName",
        "dn_attribute_name": "dnAttributeName",
        "connection_timeout": "connectionTimeout",
    }

    def __init__(
        self,
        search_user_name=None,
        search_user_password=None,
        server_url=None,
        base_dn=None,
        username_attribute_name=None,
        dn_attribute_name=None,
        connection_timeout=None,
        _configuration=None,
    ):  # noqa: E501
        """FtsLdapAuthenticationDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._search_user_name = None
        self._search_user_password = None
        self._server_url = None
        self._base_dn = None
        self._username_attribute_name = None
        self._dn_attribute_name = None
        self._connection_timeout = None
        self.discriminator = None

        if search_user_name is not None:
            self.search_user_name = search_user_name
        if search_user_password is not None:
            self.search_user_password = search_user_password
        if server_url is not None:
            self.server_url = server_url
        if base_dn is not None:
            self.base_dn = base_dn
        if username_attribute_name is not None:
            self.username_attribute_name = username_attribute_name
        if dn_attribute_name is not None:
            self.dn_attribute_name = dn_attribute_name
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout

    @property
    def search_user_name(self):
        """Gets the search_user_name of this FtsLdapAuthenticationDetails.  # noqa: E501

        Name of the user that runs the search action for users that log on  # noqa: E501

        :return: The search_user_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._search_user_name

    @search_user_name.setter
    def search_user_name(self, search_user_name):
        """Sets the search_user_name of this FtsLdapAuthenticationDetails.

        Name of the user that runs the search action for users that log on  # noqa: E501

        :param search_user_name: The search_user_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._search_user_name = search_user_name

    @property
    def search_user_password(self):
        """Gets the search_user_password of this FtsLdapAuthenticationDetails.  # noqa: E501

        Password of the user that runs the search action for users that log on  # noqa: E501

        :return: The search_user_password of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._search_user_password

    @search_user_password.setter
    def search_user_password(self, search_user_password):
        """Sets the search_user_password of this FtsLdapAuthenticationDetails.

        Password of the user that runs the search action for users that log on  # noqa: E501

        :param search_user_password: The search_user_password of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._search_user_password = search_user_password

    @property
    def server_url(self):
        """Gets the server_url of this FtsLdapAuthenticationDetails.  # noqa: E501

        URL of the LDAP Directory server  # noqa: E501

        :return: The server_url of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this FtsLdapAuthenticationDetails.

        URL of the LDAP Directory server  # noqa: E501

        :param server_url: The server_url of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._server_url = server_url

    @property
    def base_dn(self):
        """Gets the base_dn of this FtsLdapAuthenticationDetails.  # noqa: E501

        Base DN (the point from where the server will search for users)  # noqa: E501

        :return: The base_dn of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this FtsLdapAuthenticationDetails.

        Base DN (the point from where the server will search for users)  # noqa: E501

        :param base_dn: The base_dn of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def username_attribute_name(self):
        """Gets the username_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501

        Name of the LDAP attribute containing the username  # noqa: E501

        :return: The username_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._username_attribute_name

    @username_attribute_name.setter
    def username_attribute_name(self, username_attribute_name):
        """Sets the username_attribute_name of this FtsLdapAuthenticationDetails.

        Name of the LDAP attribute containing the username  # noqa: E501

        :param username_attribute_name: The username_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._username_attribute_name = username_attribute_name

    @property
    def dn_attribute_name(self):
        """Gets the dn_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501

        Name of the LDAP attribute containing the distinguished name  # noqa: E501

        :return: The dn_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: str
        """
        return self._dn_attribute_name

    @dn_attribute_name.setter
    def dn_attribute_name(self, dn_attribute_name):
        """Sets the dn_attribute_name of this FtsLdapAuthenticationDetails.

        Name of the LDAP attribute containing the distinguished name  # noqa: E501

        :param dn_attribute_name: The dn_attribute_name of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: str
        """

        self._dn_attribute_name = dn_attribute_name

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this FtsLdapAuthenticationDetails.  # noqa: E501

        LDAP server connection timeout in milliseconds  # noqa: E501

        :return: The connection_timeout of this FtsLdapAuthenticationDetails.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this FtsLdapAuthenticationDetails.

        LDAP server connection timeout in milliseconds  # noqa: E501

        :param connection_timeout: The connection_timeout of this FtsLdapAuthenticationDetails.  # noqa: E501
        :type: int
        """

        self._connection_timeout = connection_timeout

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
        if issubclass(FtsLdapAuthenticationDetails, dict):
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
        if not isinstance(other, FtsLdapAuthenticationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FtsLdapAuthenticationDetails):
            return True

        return self.to_dict() != other.to_dict()
