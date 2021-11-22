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


class MftConfigurationData(object):
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
        'connection_timeout_in_seconds': 'int',
        'connection_retries': 'int',
        'connection_time_between_retries_in_seconds': 'int',
        'debug_level': 'int',
        'pgp_temp_dir': 'str',
        'ssl_debug_trace': 'bool',
        'pam_authentication': 'bool',
        'proxy_is_in_use': 'bool',
        'proxy_host': 'str',
        'proxy_port': 'int',
        'proxy_user': 'str',
        'proxy_password': 'str',
        'file_watcher_search_interval': 'int',
        'file_watcher_static_iterations': 'int',
        'file_watcher_check_file_is_in_use': 'bool',
        'file_actions_retries_interval_in_seconds': 'int',
        'file_actions_retries_num': 'int'
    }

    attribute_map = {
        'connection_timeout_in_seconds': 'connectionTimeoutInSeconds',
        'connection_retries': 'connectionRetries',
        'connection_time_between_retries_in_seconds': 'connectionTimeBetweenRetriesInSeconds',
        'debug_level': 'debugLevel',
        'pgp_temp_dir': 'pgpTempDir',
        'ssl_debug_trace': 'sslDebugTrace',
        'pam_authentication': 'pamAuthentication',
        'proxy_is_in_use': 'proxyIsInUse',
        'proxy_host': 'proxyHost',
        'proxy_port': 'proxyPort',
        'proxy_user': 'proxyUser',
        'proxy_password': 'proxyPassword',
        'file_watcher_search_interval': 'fileWatcherSearchInterval',
        'file_watcher_static_iterations': 'fileWatcherStaticIterations',
        'file_watcher_check_file_is_in_use': 'fileWatcherCheckFileIsInUse',
        'file_actions_retries_interval_in_seconds': 'fileActionsRetriesIntervalInSeconds',
        'file_actions_retries_num': 'fileActionsRetriesNum'
    }

    def __init__(self, connection_timeout_in_seconds=None, connection_retries=None, connection_time_between_retries_in_seconds=None, debug_level=None, pgp_temp_dir=None, ssl_debug_trace=None, pam_authentication=None, proxy_is_in_use=None, proxy_host=None, proxy_port=None, proxy_user=None, proxy_password=None, file_watcher_search_interval=None, file_watcher_static_iterations=None, file_watcher_check_file_is_in_use=None, file_actions_retries_interval_in_seconds=None, file_actions_retries_num=None, _configuration=None):  # noqa: E501
        """MftConfigurationData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_timeout_in_seconds = None
        self._connection_retries = None
        self._connection_time_between_retries_in_seconds = None
        self._debug_level = None
        self._pgp_temp_dir = None
        self._ssl_debug_trace = None
        self._pam_authentication = None
        self._proxy_is_in_use = None
        self._proxy_host = None
        self._proxy_port = None
        self._proxy_user = None
        self._proxy_password = None
        self._file_watcher_search_interval = None
        self._file_watcher_static_iterations = None
        self._file_watcher_check_file_is_in_use = None
        self._file_actions_retries_interval_in_seconds = None
        self._file_actions_retries_num = None
        self.discriminator = None

        if connection_timeout_in_seconds is not None:
            self.connection_timeout_in_seconds = connection_timeout_in_seconds
        if connection_retries is not None:
            self.connection_retries = connection_retries
        if connection_time_between_retries_in_seconds is not None:
            self.connection_time_between_retries_in_seconds = connection_time_between_retries_in_seconds
        if debug_level is not None:
            self.debug_level = debug_level
        if pgp_temp_dir is not None:
            self.pgp_temp_dir = pgp_temp_dir
        if ssl_debug_trace is not None:
            self.ssl_debug_trace = ssl_debug_trace
        if pam_authentication is not None:
            self.pam_authentication = pam_authentication
        if proxy_is_in_use is not None:
            self.proxy_is_in_use = proxy_is_in_use
        if proxy_host is not None:
            self.proxy_host = proxy_host
        if proxy_port is not None:
            self.proxy_port = proxy_port
        if proxy_user is not None:
            self.proxy_user = proxy_user
        if proxy_password is not None:
            self.proxy_password = proxy_password
        if file_watcher_search_interval is not None:
            self.file_watcher_search_interval = file_watcher_search_interval
        if file_watcher_static_iterations is not None:
            self.file_watcher_static_iterations = file_watcher_static_iterations
        if file_watcher_check_file_is_in_use is not None:
            self.file_watcher_check_file_is_in_use = file_watcher_check_file_is_in_use
        if file_actions_retries_interval_in_seconds is not None:
            self.file_actions_retries_interval_in_seconds = file_actions_retries_interval_in_seconds
        if file_actions_retries_num is not None:
            self.file_actions_retries_num = file_actions_retries_num

    @property
    def connection_timeout_in_seconds(self):
        """Gets the connection_timeout_in_seconds of this MftConfigurationData.  # noqa: E501

        Connection timeout (seconds) HIDDEN  # noqa: E501

        :return: The connection_timeout_in_seconds of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout_in_seconds

    @connection_timeout_in_seconds.setter
    def connection_timeout_in_seconds(self, connection_timeout_in_seconds):
        """Sets the connection_timeout_in_seconds of this MftConfigurationData.

        Connection timeout (seconds) HIDDEN  # noqa: E501

        :param connection_timeout_in_seconds: The connection_timeout_in_seconds of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._connection_timeout_in_seconds = connection_timeout_in_seconds

    @property
    def connection_retries(self):
        """Gets the connection_retries of this MftConfigurationData.  # noqa: E501

        Number of connection retries HIDDEN  # noqa: E501

        :return: The connection_retries of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._connection_retries

    @connection_retries.setter
    def connection_retries(self, connection_retries):
        """Sets the connection_retries of this MftConfigurationData.

        Number of connection retries HIDDEN  # noqa: E501

        :param connection_retries: The connection_retries of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._connection_retries = connection_retries

    @property
    def connection_time_between_retries_in_seconds(self):
        """Gets the connection_time_between_retries_in_seconds of this MftConfigurationData.  # noqa: E501

        Time between connection retries (seconds) HIDDEN  # noqa: E501

        :return: The connection_time_between_retries_in_seconds of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._connection_time_between_retries_in_seconds

    @connection_time_between_retries_in_seconds.setter
    def connection_time_between_retries_in_seconds(self, connection_time_between_retries_in_seconds):
        """Sets the connection_time_between_retries_in_seconds of this MftConfigurationData.

        Time between connection retries (seconds) HIDDEN  # noqa: E501

        :param connection_time_between_retries_in_seconds: The connection_time_between_retries_in_seconds of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._connection_time_between_retries_in_seconds = connection_time_between_retries_in_seconds

    @property
    def debug_level(self):
        """Gets the debug_level of this MftConfigurationData.  # noqa: E501

        MFT debug level (0-5) HIDDEN  # noqa: E501

        :return: The debug_level of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._debug_level

    @debug_level.setter
    def debug_level(self, debug_level):
        """Sets the debug_level of this MftConfigurationData.

        MFT debug level (0-5) HIDDEN  # noqa: E501

        :param debug_level: The debug_level of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._debug_level = debug_level

    @property
    def pgp_temp_dir(self):
        """Gets the pgp_temp_dir of this MftConfigurationData.  # noqa: E501

        PGP temporary directory HIDDEN  # noqa: E501

        :return: The pgp_temp_dir of this MftConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._pgp_temp_dir

    @pgp_temp_dir.setter
    def pgp_temp_dir(self, pgp_temp_dir):
        """Sets the pgp_temp_dir of this MftConfigurationData.

        PGP temporary directory HIDDEN  # noqa: E501

        :param pgp_temp_dir: The pgp_temp_dir of this MftConfigurationData.  # noqa: E501
        :type: str
        """

        self._pgp_temp_dir = pgp_temp_dir

    @property
    def ssl_debug_trace(self):
        """Gets the ssl_debug_trace of this MftConfigurationData.  # noqa: E501

        Enable SSL debug trace HIDDEN  # noqa: E501

        :return: The ssl_debug_trace of this MftConfigurationData.  # noqa: E501
        :rtype: bool
        """
        return self._ssl_debug_trace

    @ssl_debug_trace.setter
    def ssl_debug_trace(self, ssl_debug_trace):
        """Sets the ssl_debug_trace of this MftConfigurationData.

        Enable SSL debug trace HIDDEN  # noqa: E501

        :param ssl_debug_trace: The ssl_debug_trace of this MftConfigurationData.  # noqa: E501
        :type: bool
        """

        self._ssl_debug_trace = ssl_debug_trace

    @property
    def pam_authentication(self):
        """Gets the pam_authentication of this MftConfigurationData.  # noqa: E501

        Use PAM password authentication HIDDEN  # noqa: E501

        :return: The pam_authentication of this MftConfigurationData.  # noqa: E501
        :rtype: bool
        """
        return self._pam_authentication

    @pam_authentication.setter
    def pam_authentication(self, pam_authentication):
        """Sets the pam_authentication of this MftConfigurationData.

        Use PAM password authentication HIDDEN  # noqa: E501

        :param pam_authentication: The pam_authentication of this MftConfigurationData.  # noqa: E501
        :type: bool
        """

        self._pam_authentication = pam_authentication

    @property
    def proxy_is_in_use(self):
        """Gets the proxy_is_in_use of this MftConfigurationData.  # noqa: E501

        Use web proxy HIDDEN  # noqa: E501

        :return: The proxy_is_in_use of this MftConfigurationData.  # noqa: E501
        :rtype: bool
        """
        return self._proxy_is_in_use

    @proxy_is_in_use.setter
    def proxy_is_in_use(self, proxy_is_in_use):
        """Sets the proxy_is_in_use of this MftConfigurationData.

        Use web proxy HIDDEN  # noqa: E501

        :param proxy_is_in_use: The proxy_is_in_use of this MftConfigurationData.  # noqa: E501
        :type: bool
        """

        self._proxy_is_in_use = proxy_is_in_use

    @property
    def proxy_host(self):
        """Gets the proxy_host of this MftConfigurationData.  # noqa: E501

        Proxy host HIDDEN  # noqa: E501

        :return: The proxy_host of this MftConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """Sets the proxy_host of this MftConfigurationData.

        Proxy host HIDDEN  # noqa: E501

        :param proxy_host: The proxy_host of this MftConfigurationData.  # noqa: E501
        :type: str
        """

        self._proxy_host = proxy_host

    @property
    def proxy_port(self):
        """Gets the proxy_port of this MftConfigurationData.  # noqa: E501

        Proxy port HIDDEN  # noqa: E501

        :return: The proxy_port of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy_port of this MftConfigurationData.

        Proxy port HIDDEN  # noqa: E501

        :param proxy_port: The proxy_port of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._proxy_port = proxy_port

    @property
    def proxy_user(self):
        """Gets the proxy_user of this MftConfigurationData.  # noqa: E501

        Proxy user HIDDEN  # noqa: E501

        :return: The proxy_user of this MftConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """Sets the proxy_user of this MftConfigurationData.

        Proxy user HIDDEN  # noqa: E501

        :param proxy_user: The proxy_user of this MftConfigurationData.  # noqa: E501
        :type: str
        """

        self._proxy_user = proxy_user

    @property
    def proxy_password(self):
        """Gets the proxy_password of this MftConfigurationData.  # noqa: E501

        Proxy password HIDDEN  # noqa: E501

        :return: The proxy_password of this MftConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, proxy_password):
        """Sets the proxy_password of this MftConfigurationData.

        Proxy password HIDDEN  # noqa: E501

        :param proxy_password: The proxy_password of this MftConfigurationData.  # noqa: E501
        :type: str
        """

        self._proxy_password = proxy_password

    @property
    def file_watcher_search_interval(self):
        """Gets the file_watcher_search_interval of this MftConfigurationData.  # noqa: E501

        File watch search interval (seconds) HIDDEN  # noqa: E501

        :return: The file_watcher_search_interval of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._file_watcher_search_interval

    @file_watcher_search_interval.setter
    def file_watcher_search_interval(self, file_watcher_search_interval):
        """Sets the file_watcher_search_interval of this MftConfigurationData.

        File watch search interval (seconds) HIDDEN  # noqa: E501

        :param file_watcher_search_interval: The file_watcher_search_interval of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._file_watcher_search_interval = file_watcher_search_interval

    @property
    def file_watcher_static_iterations(self):
        """Gets the file_watcher_static_iterations of this MftConfigurationData.  # noqa: E501

        Number of iterations while file is static HIDDEN  # noqa: E501

        :return: The file_watcher_static_iterations of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._file_watcher_static_iterations

    @file_watcher_static_iterations.setter
    def file_watcher_static_iterations(self, file_watcher_static_iterations):
        """Sets the file_watcher_static_iterations of this MftConfigurationData.

        Number of iterations while file is static HIDDEN  # noqa: E501

        :param file_watcher_static_iterations: The file_watcher_static_iterations of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._file_watcher_static_iterations = file_watcher_static_iterations

    @property
    def file_watcher_check_file_is_in_use(self):
        """Gets the file_watcher_check_file_is_in_use of this MftConfigurationData.  # noqa: E501

        Check that file is not in use HIDDEN  # noqa: E501

        :return: The file_watcher_check_file_is_in_use of this MftConfigurationData.  # noqa: E501
        :rtype: bool
        """
        return self._file_watcher_check_file_is_in_use

    @file_watcher_check_file_is_in_use.setter
    def file_watcher_check_file_is_in_use(self, file_watcher_check_file_is_in_use):
        """Sets the file_watcher_check_file_is_in_use of this MftConfigurationData.

        Check that file is not in use HIDDEN  # noqa: E501

        :param file_watcher_check_file_is_in_use: The file_watcher_check_file_is_in_use of this MftConfigurationData.  # noqa: E501
        :type: bool
        """

        self._file_watcher_check_file_is_in_use = file_watcher_check_file_is_in_use

    @property
    def file_actions_retries_interval_in_seconds(self):
        """Gets the file_actions_retries_interval_in_seconds of this MftConfigurationData.  # noqa: E501

        File action retry interval (seconds) HIDDEN  # noqa: E501

        :return: The file_actions_retries_interval_in_seconds of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._file_actions_retries_interval_in_seconds

    @file_actions_retries_interval_in_seconds.setter
    def file_actions_retries_interval_in_seconds(self, file_actions_retries_interval_in_seconds):
        """Sets the file_actions_retries_interval_in_seconds of this MftConfigurationData.

        File action retry interval (seconds) HIDDEN  # noqa: E501

        :param file_actions_retries_interval_in_seconds: The file_actions_retries_interval_in_seconds of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._file_actions_retries_interval_in_seconds = file_actions_retries_interval_in_seconds

    @property
    def file_actions_retries_num(self):
        """Gets the file_actions_retries_num of this MftConfigurationData.  # noqa: E501

        Number of file action retries HIDDEN  # noqa: E501

        :return: The file_actions_retries_num of this MftConfigurationData.  # noqa: E501
        :rtype: int
        """
        return self._file_actions_retries_num

    @file_actions_retries_num.setter
    def file_actions_retries_num(self, file_actions_retries_num):
        """Sets the file_actions_retries_num of this MftConfigurationData.

        Number of file action retries HIDDEN  # noqa: E501

        :param file_actions_retries_num: The file_actions_retries_num of this MftConfigurationData.  # noqa: E501
        :type: int
        """

        self._file_actions_retries_num = file_actions_retries_num

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
        if issubclass(MftConfigurationData, dict):
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
        if not isinstance(other, MftConfigurationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MftConfigurationData):
            return True

        return self.to_dict() != other.to_dict()
