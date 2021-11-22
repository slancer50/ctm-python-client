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


class FtsFtpSettings(object):
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
        "server_enabled": "bool",
        "port": "int",
        "authentication_method": "str",
        "secured": "bool",
        "keystore_file_path": "str",
        "keystore_file_password": "str",
        "ciphers": "str",
        "listen_for_implicit_connection": "bool",
        "passive_ports": "str",
    }

    attribute_map = {
        "server_enabled": "serverEnabled",
        "port": "port",
        "authentication_method": "authenticationMethod",
        "secured": "secured",
        "keystore_file_path": "keystoreFilePath",
        "keystore_file_password": "keystoreFilePassword",
        "ciphers": "ciphers",
        "listen_for_implicit_connection": "listenForImplicitConnection",
        "passive_ports": "passivePorts",
    }

    def __init__(
        self,
        server_enabled=None,
        port=None,
        authentication_method=None,
        secured=None,
        keystore_file_path=None,
        keystore_file_password=None,
        ciphers=None,
        listen_for_implicit_connection=None,
        passive_ports=None,
        _configuration=None,
    ):  # noqa: E501
        """FtsFtpSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._server_enabled = None
        self._port = None
        self._authentication_method = None
        self._secured = None
        self._keystore_file_path = None
        self._keystore_file_password = None
        self._ciphers = None
        self._listen_for_implicit_connection = None
        self._passive_ports = None
        self.discriminator = None

        if server_enabled is not None:
            self.server_enabled = server_enabled
        if port is not None:
            self.port = port
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if secured is not None:
            self.secured = secured
        if keystore_file_path is not None:
            self.keystore_file_path = keystore_file_path
        if keystore_file_password is not None:
            self.keystore_file_password = keystore_file_password
        if ciphers is not None:
            self.ciphers = ciphers
        if listen_for_implicit_connection is not None:
            self.listen_for_implicit_connection = listen_for_implicit_connection
        if passive_ports is not None:
            self.passive_ports = passive_ports

    @property
    def server_enabled(self):
        """Gets the server_enabled of this FtsFtpSettings.  # noqa: E501

        Enable/Disable listening for FTP/S connection  # noqa: E501

        :return: The server_enabled of this FtsFtpSettings.  # noqa: E501
        :rtype: bool
        """
        return self._server_enabled

    @server_enabled.setter
    def server_enabled(self, server_enabled):
        """Sets the server_enabled of this FtsFtpSettings.

        Enable/Disable listening for FTP/S connection  # noqa: E501

        :param server_enabled: The server_enabled of this FtsFtpSettings.  # noqa: E501
        :type: bool
        """

        self._server_enabled = server_enabled

    @property
    def port(self):
        """Gets the port of this FtsFtpSettings.  # noqa: E501

        FTP server port  # noqa: E501

        :return: The port of this FtsFtpSettings.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FtsFtpSettings.

        FTP server port  # noqa: E501

        :param port: The port of this FtsFtpSettings.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def authentication_method(self):
        """Gets the authentication_method of this FtsFtpSettings.  # noqa: E501

        Authentication method being used to connect FTP server  # noqa: E501

        :return: The authentication_method of this FtsFtpSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this FtsFtpSettings.

        Authentication method being used to connect FTP server  # noqa: E501

        :param authentication_method: The authentication_method of this FtsFtpSettings.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def secured(self):
        """Gets the secured of this FtsFtpSettings.  # noqa: E501

        Use FTP secure connection (SSL/TLS)  # noqa: E501

        :return: The secured of this FtsFtpSettings.  # noqa: E501
        :rtype: bool
        """
        return self._secured

    @secured.setter
    def secured(self, secured):
        """Sets the secured of this FtsFtpSettings.

        Use FTP secure connection (SSL/TLS)  # noqa: E501

        :param secured: The secured of this FtsFtpSettings.  # noqa: E501
        :type: bool
        """

        self._secured = secured

    @property
    def keystore_file_path(self):
        """Gets the keystore_file_path of this FtsFtpSettings.  # noqa: E501

        FTPS keystore file location  # noqa: E501

        :return: The keystore_file_path of this FtsFtpSettings.  # noqa: E501
        :rtype: str
        """
        return self._keystore_file_path

    @keystore_file_path.setter
    def keystore_file_path(self, keystore_file_path):
        """Sets the keystore_file_path of this FtsFtpSettings.

        FTPS keystore file location  # noqa: E501

        :param keystore_file_path: The keystore_file_path of this FtsFtpSettings.  # noqa: E501
        :type: str
        """

        self._keystore_file_path = keystore_file_path

    @property
    def keystore_file_password(self):
        """Gets the keystore_file_password of this FtsFtpSettings.  # noqa: E501

        Password being used to access the FTPS keystore  # noqa: E501

        :return: The keystore_file_password of this FtsFtpSettings.  # noqa: E501
        :rtype: str
        """
        return self._keystore_file_password

    @keystore_file_password.setter
    def keystore_file_password(self, keystore_file_password):
        """Sets the keystore_file_password of this FtsFtpSettings.

        Password being used to access the FTPS keystore  # noqa: E501

        :param keystore_file_password: The keystore_file_password of this FtsFtpSettings.  # noqa: E501
        :type: str
        """

        self._keystore_file_password = keystore_file_password

    @property
    def ciphers(self):
        """Gets the ciphers of this FtsFtpSettings.  # noqa: E501

        Ftps server allowed cipher suites (comma-separated). Leave empty to allow all supported cipher suites.  # noqa: E501

        :return: The ciphers of this FtsFtpSettings.  # noqa: E501
        :rtype: str
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this FtsFtpSettings.

        Ftps server allowed cipher suites (comma-separated). Leave empty to allow all supported cipher suites.  # noqa: E501

        :param ciphers: The ciphers of this FtsFtpSettings.  # noqa: E501
        :type: str
        """

        self._ciphers = ciphers

    @property
    def listen_for_implicit_connection(self):
        """Gets the listen_for_implicit_connection of this FtsFtpSettings.  # noqa: E501

        Implicit negotiation mode - requires that the entire FTP session must be encrypted  # noqa: E501

        :return: The listen_for_implicit_connection of this FtsFtpSettings.  # noqa: E501
        :rtype: bool
        """
        return self._listen_for_implicit_connection

    @listen_for_implicit_connection.setter
    def listen_for_implicit_connection(self, listen_for_implicit_connection):
        """Sets the listen_for_implicit_connection of this FtsFtpSettings.

        Implicit negotiation mode - requires that the entire FTP session must be encrypted  # noqa: E501

        :param listen_for_implicit_connection: The listen_for_implicit_connection of this FtsFtpSettings.  # noqa: E501
        :type: bool
        """

        self._listen_for_implicit_connection = listen_for_implicit_connection

    @property
    def passive_ports(self):
        """Gets the passive_ports of this FtsFtpSettings.  # noqa: E501

        Passive FTP ports range - for PASV connections, the server will open a random port in this range for client to connect to  # noqa: E501

        :return: The passive_ports of this FtsFtpSettings.  # noqa: E501
        :rtype: str
        """
        return self._passive_ports

    @passive_ports.setter
    def passive_ports(self, passive_ports):
        """Sets the passive_ports of this FtsFtpSettings.

        Passive FTP ports range - for PASV connections, the server will open a random port in this range for client to connect to  # noqa: E501

        :param passive_ports: The passive_ports of this FtsFtpSettings.  # noqa: E501
        :type: str
        """

        self._passive_ports = passive_ports

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
        if issubclass(FtsFtpSettings, dict):
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
        if not isinstance(other, FtsFtpSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FtsFtpSettings):
            return True

        return self.to_dict() != other.to_dict()
