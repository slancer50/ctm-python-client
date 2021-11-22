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


class HubData(object):
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
        "status": "str",
        "sync_status": "str",
        "name": "str",
        "cpu": "str",
        "memory": "str",
        "message": "str",
    }

    attribute_map = {
        "status": "status",
        "sync_status": "syncStatus",
        "name": "name",
        "cpu": "cpu",
        "memory": "memory",
        "message": "message",
    }

    def __init__(
        self,
        status=None,
        sync_status=None,
        name=None,
        cpu=None,
        memory=None,
        message=None,
        _configuration=None,
    ):  # noqa: E501
        """HubData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._sync_status = None
        self._name = None
        self._cpu = None
        self._memory = None
        self._message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if sync_status is not None:
            self.sync_status = sync_status
        if name is not None:
            self.name = name
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if message is not None:
            self.message = message

    @property
    def status(self):
        """Gets the status of this HubData.  # noqa: E501

        Hub state  # noqa: E501

        :return: The status of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HubData.

        Hub state  # noqa: E501

        :param status: The status of this HubData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sync_status(self):
        """Gets the sync_status of this HubData.  # noqa: E501

        Hub sync status  # noqa: E501

        :return: The sync_status of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this HubData.

        Hub sync status  # noqa: E501

        :param sync_status: The sync_status of this HubData.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

    @property
    def name(self):
        """Gets the name of this HubData.  # noqa: E501

        Agent name  # noqa: E501

        :return: The name of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HubData.

        Agent name  # noqa: E501

        :param name: The name of this HubData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cpu(self):
        """Gets the cpu of this HubData.  # noqa: E501

        CPU  # noqa: E501

        :return: The cpu of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this HubData.

        CPU  # noqa: E501

        :param cpu: The cpu of this HubData.  # noqa: E501
        :type: str
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this HubData.  # noqa: E501

        memory usage  # noqa: E501

        :return: The memory of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this HubData.

        memory usage  # noqa: E501

        :param memory: The memory of this HubData.  # noqa: E501
        :type: str
        """

        self._memory = memory

    @property
    def message(self):
        """Gets the message of this HubData.  # noqa: E501

        Hub Health Message  # noqa: E501

        :return: The message of this HubData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HubData.

        Hub Health Message  # noqa: E501

        :param message: The message of this HubData.  # noqa: E501
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
        if issubclass(HubData, dict):
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
        if not isinstance(other, HubData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubData):
            return True

        return self.to_dict() != other.to_dict()
