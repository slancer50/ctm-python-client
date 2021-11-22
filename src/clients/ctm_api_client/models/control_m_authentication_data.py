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


class ControlMAuthenticationData(object):
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
        "password": "str",
        "password_expiration_days": "int",
        "change_password_at_next_login": "bool",
        "lock_account": "bool",
        "account_locked_on_date": "str",
    }

    attribute_map = {
        "password": "Password",
        "password_expiration_days": "PasswordExpirationDays",
        "change_password_at_next_login": "ChangePasswordAtNextLogin",
        "lock_account": "LockAccount",
        "account_locked_on_date": "AccountLockedOnDate",
    }

    def __init__(
        self,
        password=None,
        password_expiration_days=None,
        change_password_at_next_login=None,
        lock_account=None,
        account_locked_on_date=None,
        _configuration=None,
    ):  # noqa: E501
        """ControlMAuthenticationData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._password = None
        self._password_expiration_days = None
        self._change_password_at_next_login = None
        self._lock_account = None
        self._account_locked_on_date = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if password_expiration_days is not None:
            self.password_expiration_days = password_expiration_days
        if change_password_at_next_login is not None:
            self.change_password_at_next_login = change_password_at_next_login
        if lock_account is not None:
            self.lock_account = lock_account
        if account_locked_on_date is not None:
            self.account_locked_on_date = account_locked_on_date

    @property
    def password(self):
        """Gets the password of this ControlMAuthenticationData.  # noqa: E501

        password or secret  # noqa: E501

        :return: The password of this ControlMAuthenticationData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ControlMAuthenticationData.

        password or secret  # noqa: E501

        :param password: The password of this ControlMAuthenticationData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_expiration_days(self):
        """Gets the password_expiration_days of this ControlMAuthenticationData.  # noqa: E501

        number of days until the password expires  # noqa: E501

        :return: The password_expiration_days of this ControlMAuthenticationData.  # noqa: E501
        :rtype: int
        """
        return self._password_expiration_days

    @password_expiration_days.setter
    def password_expiration_days(self, password_expiration_days):
        """Sets the password_expiration_days of this ControlMAuthenticationData.

        number of days until the password expires  # noqa: E501

        :param password_expiration_days: The password_expiration_days of this ControlMAuthenticationData.  # noqa: E501
        :type: int
        """

        self._password_expiration_days = password_expiration_days

    @property
    def change_password_at_next_login(self):
        """Gets the change_password_at_next_login of this ControlMAuthenticationData.  # noqa: E501

        should password be changed in next login  # noqa: E501

        :return: The change_password_at_next_login of this ControlMAuthenticationData.  # noqa: E501
        :rtype: bool
        """
        return self._change_password_at_next_login

    @change_password_at_next_login.setter
    def change_password_at_next_login(self, change_password_at_next_login):
        """Sets the change_password_at_next_login of this ControlMAuthenticationData.

        should password be changed in next login  # noqa: E501

        :param change_password_at_next_login: The change_password_at_next_login of this ControlMAuthenticationData.  # noqa: E501
        :type: bool
        """

        self._change_password_at_next_login = change_password_at_next_login

    @property
    def lock_account(self):
        """Gets the lock_account of this ControlMAuthenticationData.  # noqa: E501

        lock account  # noqa: E501

        :return: The lock_account of this ControlMAuthenticationData.  # noqa: E501
        :rtype: bool
        """
        return self._lock_account

    @lock_account.setter
    def lock_account(self, lock_account):
        """Sets the lock_account of this ControlMAuthenticationData.

        lock account  # noqa: E501

        :param lock_account: The lock_account of this ControlMAuthenticationData.  # noqa: E501
        :type: bool
        """

        self._lock_account = lock_account

    @property
    def account_locked_on_date(self):
        """Gets the account_locked_on_date of this ControlMAuthenticationData.  # noqa: E501

        account locked on date  # noqa: E501

        :return: The account_locked_on_date of this ControlMAuthenticationData.  # noqa: E501
        :rtype: str
        """
        return self._account_locked_on_date

    @account_locked_on_date.setter
    def account_locked_on_date(self, account_locked_on_date):
        """Sets the account_locked_on_date of this ControlMAuthenticationData.

        account locked on date  # noqa: E501

        :param account_locked_on_date: The account_locked_on_date of this ControlMAuthenticationData.  # noqa: E501
        :type: str
        """

        self._account_locked_on_date = account_locked_on_date

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
        if issubclass(ControlMAuthenticationData, dict):
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
        if not isinstance(other, ControlMAuthenticationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlMAuthenticationData):
            return True

        return self.to_dict() != other.to_dict()
