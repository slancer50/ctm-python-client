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


class AuthenticateCredentials(object):
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
        'username': 'str',
        'msg': 'str',
        'sessiontoken': 'str',
        'groups': 'list[str]',
        'additional_attributes': 'list[object]'
    }

    attribute_map = {
        'username': 'username',
        'msg': 'msg',
        'sessiontoken': 'sessiontoken',
        'groups': 'groups',
        'additional_attributes': 'additionalAttributes'
    }

    def __init__(self, username=None, msg=None, sessiontoken=None, groups=None, additional_attributes=None, _configuration=None):  # noqa: E501
        """AuthenticateCredentials - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username = None
        self._msg = None
        self._sessiontoken = None
        self._groups = None
        self._additional_attributes = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if msg is not None:
            self.msg = msg
        if sessiontoken is not None:
            self.sessiontoken = sessiontoken
        if groups is not None:
            self.groups = groups
        if additional_attributes is not None:
            self.additional_attributes = additional_attributes

    @property
    def username(self):
        """Gets the username of this AuthenticateCredentials.  # noqa: E501


        :return: The username of this AuthenticateCredentials.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthenticateCredentials.


        :param username: The username of this AuthenticateCredentials.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def msg(self):
        """Gets the msg of this AuthenticateCredentials.  # noqa: E501


        :return: The msg of this AuthenticateCredentials.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this AuthenticateCredentials.


        :param msg: The msg of this AuthenticateCredentials.  # noqa: E501
        :type: str
        """

        self._msg = msg

    @property
    def sessiontoken(self):
        """Gets the sessiontoken of this AuthenticateCredentials.  # noqa: E501


        :return: The sessiontoken of this AuthenticateCredentials.  # noqa: E501
        :rtype: str
        """
        return self._sessiontoken

    @sessiontoken.setter
    def sessiontoken(self, sessiontoken):
        """Sets the sessiontoken of this AuthenticateCredentials.


        :param sessiontoken: The sessiontoken of this AuthenticateCredentials.  # noqa: E501
        :type: str
        """

        self._sessiontoken = sessiontoken

    @property
    def groups(self):
        """Gets the groups of this AuthenticateCredentials.  # noqa: E501


        :return: The groups of this AuthenticateCredentials.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AuthenticateCredentials.


        :param groups: The groups of this AuthenticateCredentials.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def additional_attributes(self):
        """Gets the additional_attributes of this AuthenticateCredentials.  # noqa: E501


        :return: The additional_attributes of this AuthenticateCredentials.  # noqa: E501
        :rtype: list[object]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """Sets the additional_attributes of this AuthenticateCredentials.


        :param additional_attributes: The additional_attributes of this AuthenticateCredentials.  # noqa: E501
        :type: list[object]
        """

        self._additional_attributes = additional_attributes

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
        if issubclass(AuthenticateCredentials, dict):
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
        if not isinstance(other, AuthenticateCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticateCredentials):
            return True

        return self.to_dict() != other.to_dict()
