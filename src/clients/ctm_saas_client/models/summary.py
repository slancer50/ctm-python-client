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


class Summary(object):
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
        'total_number_of_jobs': 'int',
        'total_data_size': 'str',
        'actual_db_size': 'str',
        'disk_usage': 'str'
    }

    attribute_map = {
        'total_number_of_jobs': 'totalNumberOfJobs',
        'total_data_size': 'totalDataSize',
        'actual_db_size': 'actualDbSize',
        'disk_usage': 'diskUsage'
    }

    def __init__(self, total_number_of_jobs=None, total_data_size=None, actual_db_size=None, disk_usage=None, _configuration=None):  # noqa: E501
        """Summary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_number_of_jobs = None
        self._total_data_size = None
        self._actual_db_size = None
        self._disk_usage = None
        self.discriminator = None

        if total_number_of_jobs is not None:
            self.total_number_of_jobs = total_number_of_jobs
        if total_data_size is not None:
            self.total_data_size = total_data_size
        if actual_db_size is not None:
            self.actual_db_size = actual_db_size
        if disk_usage is not None:
            self.disk_usage = disk_usage

    @property
    def total_number_of_jobs(self):
        """Gets the total_number_of_jobs of this Summary.  # noqa: E501


        :return: The total_number_of_jobs of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_jobs

    @total_number_of_jobs.setter
    def total_number_of_jobs(self, total_number_of_jobs):
        """Sets the total_number_of_jobs of this Summary.


        :param total_number_of_jobs: The total_number_of_jobs of this Summary.  # noqa: E501
        :type: int
        """

        self._total_number_of_jobs = total_number_of_jobs

    @property
    def total_data_size(self):
        """Gets the total_data_size of this Summary.  # noqa: E501


        :return: The total_data_size of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_data_size

    @total_data_size.setter
    def total_data_size(self, total_data_size):
        """Sets the total_data_size of this Summary.


        :param total_data_size: The total_data_size of this Summary.  # noqa: E501
        :type: str
        """

        self._total_data_size = total_data_size

    @property
    def actual_db_size(self):
        """Gets the actual_db_size of this Summary.  # noqa: E501


        :return: The actual_db_size of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._actual_db_size

    @actual_db_size.setter
    def actual_db_size(self, actual_db_size):
        """Sets the actual_db_size of this Summary.


        :param actual_db_size: The actual_db_size of this Summary.  # noqa: E501
        :type: str
        """

        self._actual_db_size = actual_db_size

    @property
    def disk_usage(self):
        """Gets the disk_usage of this Summary.  # noqa: E501


        :return: The disk_usage of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        """Sets the disk_usage of this Summary.


        :param disk_usage: The disk_usage of this Summary.  # noqa: E501
        :type: str
        """

        self._disk_usage = disk_usage

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
        if issubclass(Summary, dict):
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
        if not isinstance(other, Summary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Summary):
            return True

        return self.to_dict() != other.to_dict()
