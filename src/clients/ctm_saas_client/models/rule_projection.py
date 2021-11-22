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


class RuleProjection(object):
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
        'description': 'str',
        'last_updated_timestamp': 'int',
        'name': 'str',
        'priority': 'int',
        'search_tags': 'list[SearchTagTuple]',
        'status': 'str'
    }

    attribute_map = {
        'description': 'description',
        'last_updated_timestamp': 'lastUpdatedTimestamp',
        'name': 'name',
        'priority': 'priority',
        'search_tags': 'searchTags',
        'status': 'status'
    }

    def __init__(self, description=None, last_updated_timestamp=None, name=None, priority=None, search_tags=None, status=None, _configuration=None):  # noqa: E501
        """RuleProjection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._last_updated_timestamp = None
        self._name = None
        self._priority = None
        self._search_tags = None
        self._status = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if last_updated_timestamp is not None:
            self.last_updated_timestamp = last_updated_timestamp
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if search_tags is not None:
            self.search_tags = search_tags
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this RuleProjection.  # noqa: E501


        :return: The description of this RuleProjection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleProjection.


        :param description: The description of this RuleProjection.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_updated_timestamp(self):
        """Gets the last_updated_timestamp of this RuleProjection.  # noqa: E501


        :return: The last_updated_timestamp of this RuleProjection.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """Sets the last_updated_timestamp of this RuleProjection.


        :param last_updated_timestamp: The last_updated_timestamp of this RuleProjection.  # noqa: E501
        :type: int
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def name(self):
        """Gets the name of this RuleProjection.  # noqa: E501


        :return: The name of this RuleProjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleProjection.


        :param name: The name of this RuleProjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this RuleProjection.  # noqa: E501


        :return: The priority of this RuleProjection.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this RuleProjection.


        :param priority: The priority of this RuleProjection.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def search_tags(self):
        """Gets the search_tags of this RuleProjection.  # noqa: E501


        :return: The search_tags of this RuleProjection.  # noqa: E501
        :rtype: list[SearchTagTuple]
        """
        return self._search_tags

    @search_tags.setter
    def search_tags(self, search_tags):
        """Sets the search_tags of this RuleProjection.


        :param search_tags: The search_tags of this RuleProjection.  # noqa: E501
        :type: list[SearchTagTuple]
        """

        self._search_tags = search_tags

    @property
    def status(self):
        """Gets the status of this RuleProjection.  # noqa: E501


        :return: The status of this RuleProjection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RuleProjection.


        :param status: The status of this RuleProjection.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(RuleProjection, dict):
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
        if not isinstance(other, RuleProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleProjection):
            return True

        return self.to_dict() != other.to_dict()
