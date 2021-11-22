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


class CtmvarErrorInfo(object):
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
        "ctmvar_del_error_code": "str",
        "ctmvar_get_error_code": "str",
        "ctmvar_set_error_code": "str",
        "variable_name": "str",
    }

    attribute_map = {
        "ctmvar_del_error_code": "ctmvar_del_error_code",
        "ctmvar_get_error_code": "ctmvar_get_error_code",
        "ctmvar_set_error_code": "ctmvar_set_error_code",
        "variable_name": "variable_name",
    }

    def __init__(
        self,
        ctmvar_del_error_code=None,
        ctmvar_get_error_code=None,
        ctmvar_set_error_code=None,
        variable_name=None,
        _configuration=None,
    ):  # noqa: E501
        """CtmvarErrorInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ctmvar_del_error_code = None
        self._ctmvar_get_error_code = None
        self._ctmvar_set_error_code = None
        self._variable_name = None
        self.discriminator = None

        if ctmvar_del_error_code is not None:
            self.ctmvar_del_error_code = ctmvar_del_error_code
        if ctmvar_get_error_code is not None:
            self.ctmvar_get_error_code = ctmvar_get_error_code
        if ctmvar_set_error_code is not None:
            self.ctmvar_set_error_code = ctmvar_set_error_code
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def ctmvar_del_error_code(self):
        """Gets the ctmvar_del_error_code of this CtmvarErrorInfo.  # noqa: E501


        :return: The ctmvar_del_error_code of this CtmvarErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctmvar_del_error_code

    @ctmvar_del_error_code.setter
    def ctmvar_del_error_code(self, ctmvar_del_error_code):
        """Sets the ctmvar_del_error_code of this CtmvarErrorInfo.


        :param ctmvar_del_error_code: The ctmvar_del_error_code of this CtmvarErrorInfo.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "FailedDeletingFromDB",
            "PoolNameInvalid",
            "UnKnownDelError",
            "UNRECOGNIZED",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and ctmvar_del_error_code not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `ctmvar_del_error_code` ({0}), must be one of {1}".format(  # noqa: E501
                    ctmvar_del_error_code, allowed_values
                )
            )

        self._ctmvar_del_error_code = ctmvar_del_error_code

    @property
    def ctmvar_get_error_code(self):
        """Gets the ctmvar_get_error_code of this CtmvarErrorInfo.  # noqa: E501


        :return: The ctmvar_get_error_code of this CtmvarErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctmvar_get_error_code

    @ctmvar_get_error_code.setter
    def ctmvar_get_error_code(self, ctmvar_get_error_code):
        """Sets the ctmvar_get_error_code of this CtmvarErrorInfo.


        :param ctmvar_get_error_code: The ctmvar_get_error_code of this CtmvarErrorInfo.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "FailedReadingFromDB",
            "PoolNameExpressionInvalid",
            "VarExpressionInvalidGet",
            "UnKnownGetError",
            "UNRECOGNIZED",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and ctmvar_get_error_code not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `ctmvar_get_error_code` ({0}), must be one of {1}".format(  # noqa: E501
                    ctmvar_get_error_code, allowed_values
                )
            )

        self._ctmvar_get_error_code = ctmvar_get_error_code

    @property
    def ctmvar_set_error_code(self):
        """Gets the ctmvar_set_error_code of this CtmvarErrorInfo.  # noqa: E501


        :return: The ctmvar_set_error_code of this CtmvarErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctmvar_set_error_code

    @ctmvar_set_error_code.setter
    def ctmvar_set_error_code(self, ctmvar_set_error_code):
        """Sets the ctmvar_set_error_code of this CtmvarErrorInfo.


        :param ctmvar_set_error_code: The ctmvar_set_error_code of this CtmvarErrorInfo.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "NoError",
            "VarNameTooLong",
            "VarNameInvalid",
            "VarExpressionTooLong",
            "VarExpressionInvalidSet",
            "VarNameIsReserved",
            "FailedWritingToDB",
            "UnKnownSetError",
            "UNRECOGNIZED",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and ctmvar_set_error_code not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `ctmvar_set_error_code` ({0}), must be one of {1}".format(  # noqa: E501
                    ctmvar_set_error_code, allowed_values
                )
            )

        self._ctmvar_set_error_code = ctmvar_set_error_code

    @property
    def variable_name(self):
        """Gets the variable_name of this CtmvarErrorInfo.  # noqa: E501


        :return: The variable_name of this CtmvarErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this CtmvarErrorInfo.


        :param variable_name: The variable_name of this CtmvarErrorInfo.  # noqa: E501
        :type: str
        """

        self._variable_name = variable_name

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
        if issubclass(CtmvarErrorInfo, dict):
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
        if not isinstance(other, CtmvarErrorInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CtmvarErrorInfo):
            return True

        return self.to_dict() != other.to_dict()
