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


class SystemSettingLdap(object):
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
        'ldap_enabled': 'bool',
        'default_domain': 'str',
        'domains': 'list[LdapDomainSettings]'
    }

    attribute_map = {
        'ldap_enabled': 'ldapEnabled',
        'default_domain': 'defaultDomain',
        'domains': 'domains'
    }

    def __init__(self, ldap_enabled=None, default_domain=None, domains=None, _configuration=None):  # noqa: E501
        """SystemSettingLdap - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ldap_enabled = None
        self._default_domain = None
        self._domains = None
        self.discriminator = None

        self.ldap_enabled = ldap_enabled
        if default_domain is not None:
            self.default_domain = default_domain
        if domains is not None:
            self.domains = domains

    @property
    def ldap_enabled(self):
        """Gets the ldap_enabled of this SystemSettingLdap.  # noqa: E501


        :return: The ldap_enabled of this SystemSettingLdap.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_enabled

    @ldap_enabled.setter
    def ldap_enabled(self, ldap_enabled):
        """Sets the ldap_enabled of this SystemSettingLdap.


        :param ldap_enabled: The ldap_enabled of this SystemSettingLdap.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and ldap_enabled is None:
            raise ValueError("Invalid value for `ldap_enabled`, must not be `None`")  # noqa: E501

        self._ldap_enabled = ldap_enabled

    @property
    def default_domain(self):
        """Gets the default_domain of this SystemSettingLdap.  # noqa: E501


        :return: The default_domain of this SystemSettingLdap.  # noqa: E501
        :rtype: str
        """
        return self._default_domain

    @default_domain.setter
    def default_domain(self, default_domain):
        """Sets the default_domain of this SystemSettingLdap.


        :param default_domain: The default_domain of this SystemSettingLdap.  # noqa: E501
        :type: str
        """

        self._default_domain = default_domain

    @property
    def domains(self):
        """Gets the domains of this SystemSettingLdap.  # noqa: E501


        :return: The domains of this SystemSettingLdap.  # noqa: E501
        :rtype: list[LdapDomainSettings]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this SystemSettingLdap.


        :param domains: The domains of this SystemSettingLdap.  # noqa: E501
        :type: list[LdapDomainSettings]
        """

        self._domains = domains

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
        if issubclass(SystemSettingLdap, dict):
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
        if not isinstance(other, SystemSettingLdap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemSettingLdap):
            return True

        return self.to_dict() != other.to_dict()
