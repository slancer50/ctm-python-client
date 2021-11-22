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


class CtmvarDelResultItem(object):
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
        'del_pool_variables_error_info': 'PoolVariablesErrorInfo'
    }

    attribute_map = {
        'del_pool_variables_error_info': 'del_pool_variables_error_info'
    }

    def __init__(self, del_pool_variables_error_info=None, _configuration=None):  # noqa: E501
        """CtmvarDelResultItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._del_pool_variables_error_info = None
        self.discriminator = None

        if del_pool_variables_error_info is not None:
            self.del_pool_variables_error_info = del_pool_variables_error_info

    @property
    def del_pool_variables_error_info(self):
        """Gets the del_pool_variables_error_info of this CtmvarDelResultItem.  # noqa: E501


        :return: The del_pool_variables_error_info of this CtmvarDelResultItem.  # noqa: E501
        :rtype: PoolVariablesErrorInfo
        """
        return self._del_pool_variables_error_info

    @del_pool_variables_error_info.setter
    def del_pool_variables_error_info(self, del_pool_variables_error_info):
        """Sets the del_pool_variables_error_info of this CtmvarDelResultItem.


        :param del_pool_variables_error_info: The del_pool_variables_error_info of this CtmvarDelResultItem.  # noqa: E501
        :type: PoolVariablesErrorInfo
        """

        self._del_pool_variables_error_info = del_pool_variables_error_info

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
        if issubclass(CtmvarDelResultItem, dict):
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
        if not isinstance(other, CtmvarDelResultItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CtmvarDelResultItem):
            return True

        return self.to_dict() != other.to_dict()
