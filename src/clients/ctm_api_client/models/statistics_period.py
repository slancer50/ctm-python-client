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


class StatisticsPeriod(object):
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
    swagger_types = {"period_tag": "str", "run_info": "StatisticsRunInfo"}

    attribute_map = {"period_tag": "periodTag", "run_info": "runInfo"}

    def __init__(
        self, period_tag=None, run_info=None, _configuration=None
    ):  # noqa: E501
        """StatisticsPeriod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._period_tag = None
        self._run_info = None
        self.discriminator = None

        if period_tag is not None:
            self.period_tag = period_tag
        if run_info is not None:
            self.run_info = run_info

    @property
    def period_tag(self):
        """Gets the period_tag of this StatisticsPeriod.  # noqa: E501

        Period tag  # noqa: E501

        :return: The period_tag of this StatisticsPeriod.  # noqa: E501
        :rtype: str
        """
        return self._period_tag

    @period_tag.setter
    def period_tag(self, period_tag):
        """Sets the period_tag of this StatisticsPeriod.

        Period tag  # noqa: E501

        :param period_tag: The period_tag of this StatisticsPeriod.  # noqa: E501
        :type: str
        """

        self._period_tag = period_tag

    @property
    def run_info(self):
        """Gets the run_info of this StatisticsPeriod.  # noqa: E501

        Statistics run information  # noqa: E501

        :return: The run_info of this StatisticsPeriod.  # noqa: E501
        :rtype: StatisticsRunInfo
        """
        return self._run_info

    @run_info.setter
    def run_info(self, run_info):
        """Sets the run_info of this StatisticsPeriod.

        Statistics run information  # noqa: E501

        :param run_info: The run_info of this StatisticsPeriod.  # noqa: E501
        :type: StatisticsRunInfo
        """

        self._run_info = run_info

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
        if issubclass(StatisticsPeriod, dict):
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
        if not isinstance(other, StatisticsPeriod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticsPeriod):
            return True

        return self.to_dict() != other.to_dict()
