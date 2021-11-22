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


class ConnectionProfileDeploymentInfo(object):
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
        "ctm_name": "str",
        "status": "str",
        "status_code": "int",
        "last_update": "str",
        "message": "str",
    }

    attribute_map = {
        "ctm_name": "ctmName",
        "status": "status",
        "status_code": "statusCode",
        "last_update": "lastUpdate",
        "message": "message",
    }

    def __init__(
        self,
        ctm_name=None,
        status=None,
        status_code=None,
        last_update=None,
        message=None,
        _configuration=None,
    ):  # noqa: E501
        """ConnectionProfileDeploymentInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ctm_name = None
        self._status = None
        self._status_code = None
        self._last_update = None
        self._message = None
        self.discriminator = None

        if ctm_name is not None:
            self.ctm_name = ctm_name
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if last_update is not None:
            self.last_update = last_update
        if message is not None:
            self.message = message

    @property
    def ctm_name(self):
        """Gets the ctm_name of this ConnectionProfileDeploymentInfo.  # noqa: E501

        The logical name of Control-M/Server  # noqa: E501

        :return: The ctm_name of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctm_name

    @ctm_name.setter
    def ctm_name(self, ctm_name):
        """Sets the ctm_name of this ConnectionProfileDeploymentInfo.

        The logical name of Control-M/Server  # noqa: E501

        :param ctm_name: The ctm_name of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :type: str
        """

        self._ctm_name = ctm_name

    @property
    def status(self):
        """Gets the status of this ConnectionProfileDeploymentInfo.  # noqa: E501

        The deployment status of connection profile  # noqa: E501

        :return: The status of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectionProfileDeploymentInfo.

        The deployment status of connection profile  # noqa: E501

        :param status: The status of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this ConnectionProfileDeploymentInfo.  # noqa: E501

        The deployment status code of connection profile  # noqa: E501

        :return: The status_code of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ConnectionProfileDeploymentInfo.

        The deployment status code of connection profile  # noqa: E501

        :param status_code: The status_code of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def last_update(self):
        """Gets the last_update of this ConnectionProfileDeploymentInfo.  # noqa: E501

        UTC date of the modification  # noqa: E501

        :return: The last_update of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ConnectionProfileDeploymentInfo.

        UTC date of the modification  # noqa: E501

        :param last_update: The last_update of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def message(self):
        """Gets the message of this ConnectionProfileDeploymentInfo.  # noqa: E501

        Status information  # noqa: E501

        :return: The message of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConnectionProfileDeploymentInfo.

        Status information  # noqa: E501

        :param message: The message of this ConnectionProfileDeploymentInfo.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(ConnectionProfileDeploymentInfo, dict):
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
        if not isinstance(other, ConnectionProfileDeploymentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionProfileDeploymentInfo):
            return True

        return self.to_dict() != other.to_dict()
