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


class LogJobResults(object):
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
        'completed_status': 'ResultsStatus',
        'error': 'ApiThrowable',
        '_from': 'int',
        'results': 'list[LogJobResultItem]',
        'to': 'int'
    }

    attribute_map = {
        'completed_status': 'completed_status',
        'error': 'error',
        '_from': 'from',
        'results': 'results',
        'to': 'to'
    }

    def __init__(self, completed_status=None, error=None, _from=None, results=None, to=None, _configuration=None):  # noqa: E501
        """LogJobResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._completed_status = None
        self._error = None
        self.__from = None
        self._results = None
        self._to = None
        self.discriminator = None

        if completed_status is not None:
            self.completed_status = completed_status
        if error is not None:
            self.error = error
        if _from is not None:
            self._from = _from
        if results is not None:
            self.results = results
        if to is not None:
            self.to = to

    @property
    def completed_status(self):
        """Gets the completed_status of this LogJobResults.  # noqa: E501


        :return: The completed_status of this LogJobResults.  # noqa: E501
        :rtype: ResultsStatus
        """
        return self._completed_status

    @completed_status.setter
    def completed_status(self, completed_status):
        """Sets the completed_status of this LogJobResults.


        :param completed_status: The completed_status of this LogJobResults.  # noqa: E501
        :type: ResultsStatus
        """

        self._completed_status = completed_status

    @property
    def error(self):
        """Gets the error of this LogJobResults.  # noqa: E501


        :return: The error of this LogJobResults.  # noqa: E501
        :rtype: ApiThrowable
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LogJobResults.


        :param error: The error of this LogJobResults.  # noqa: E501
        :type: ApiThrowable
        """

        self._error = error

    @property
    def _from(self):
        """Gets the _from of this LogJobResults.  # noqa: E501


        :return: The _from of this LogJobResults.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this LogJobResults.


        :param _from: The _from of this LogJobResults.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def results(self):
        """Gets the results of this LogJobResults.  # noqa: E501


        :return: The results of this LogJobResults.  # noqa: E501
        :rtype: list[LogJobResultItem]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this LogJobResults.


        :param results: The results of this LogJobResults.  # noqa: E501
        :type: list[LogJobResultItem]
        """

        self._results = results

    @property
    def to(self):
        """Gets the to of this LogJobResults.  # noqa: E501


        :return: The to of this LogJobResults.  # noqa: E501
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this LogJobResults.


        :param to: The to of this LogJobResults.  # noqa: E501
        :type: int
        """

        self._to = to

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
        if issubclass(LogJobResults, dict):
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
        if not isinstance(other, LogJobResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogJobResults):
            return True

        return self.to_dict() != other.to_dict()
