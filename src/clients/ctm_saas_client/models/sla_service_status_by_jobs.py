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


class SLAServiceStatusByJobs(object):
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
        'executed': 'str',
        'wait_condition': 'str',
        'wait_resource': 'str',
        'wait_user': 'str',
        'wait_host': 'str',
        'wait_workload': 'str',
        'completed': 'str',
        'error': 'str',
        'unknown': 'str'
    }

    attribute_map = {
        'executed': 'executed',
        'wait_condition': 'waitCondition',
        'wait_resource': 'waitResource',
        'wait_user': 'waitUser',
        'wait_host': 'waitHost',
        'wait_workload': 'waitWorkload',
        'completed': 'completed',
        'error': 'error',
        'unknown': 'unknown'
    }

    def __init__(self, executed=None, wait_condition=None, wait_resource=None, wait_user=None, wait_host=None, wait_workload=None, completed=None, error=None, unknown=None, _configuration=None):  # noqa: E501
        """SLAServiceStatusByJobs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._executed = None
        self._wait_condition = None
        self._wait_resource = None
        self._wait_user = None
        self._wait_host = None
        self._wait_workload = None
        self._completed = None
        self._error = None
        self._unknown = None
        self.discriminator = None

        if executed is not None:
            self.executed = executed
        if wait_condition is not None:
            self.wait_condition = wait_condition
        if wait_resource is not None:
            self.wait_resource = wait_resource
        if wait_user is not None:
            self.wait_user = wait_user
        if wait_host is not None:
            self.wait_host = wait_host
        if wait_workload is not None:
            self.wait_workload = wait_workload
        if completed is not None:
            self.completed = completed
        if error is not None:
            self.error = error
        if unknown is not None:
            self.unknown = unknown

    @property
    def executed(self):
        """Gets the executed of this SLAServiceStatusByJobs.  # noqa: E501

        Executed  # noqa: E501

        :return: The executed of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._executed

    @executed.setter
    def executed(self, executed):
        """Sets the executed of this SLAServiceStatusByJobs.

        Executed  # noqa: E501

        :param executed: The executed of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._executed = executed

    @property
    def wait_condition(self):
        """Gets the wait_condition of this SLAServiceStatusByJobs.  # noqa: E501

        Wait Condition  # noqa: E501

        :return: The wait_condition of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._wait_condition

    @wait_condition.setter
    def wait_condition(self, wait_condition):
        """Sets the wait_condition of this SLAServiceStatusByJobs.

        Wait Condition  # noqa: E501

        :param wait_condition: The wait_condition of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._wait_condition = wait_condition

    @property
    def wait_resource(self):
        """Gets the wait_resource of this SLAServiceStatusByJobs.  # noqa: E501

        Wait Resource  # noqa: E501

        :return: The wait_resource of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._wait_resource

    @wait_resource.setter
    def wait_resource(self, wait_resource):
        """Sets the wait_resource of this SLAServiceStatusByJobs.

        Wait Resource  # noqa: E501

        :param wait_resource: The wait_resource of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._wait_resource = wait_resource

    @property
    def wait_user(self):
        """Gets the wait_user of this SLAServiceStatusByJobs.  # noqa: E501

        Wait User  # noqa: E501

        :return: The wait_user of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._wait_user

    @wait_user.setter
    def wait_user(self, wait_user):
        """Sets the wait_user of this SLAServiceStatusByJobs.

        Wait User  # noqa: E501

        :param wait_user: The wait_user of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._wait_user = wait_user

    @property
    def wait_host(self):
        """Gets the wait_host of this SLAServiceStatusByJobs.  # noqa: E501

        Wait Host  # noqa: E501

        :return: The wait_host of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._wait_host

    @wait_host.setter
    def wait_host(self, wait_host):
        """Sets the wait_host of this SLAServiceStatusByJobs.

        Wait Host  # noqa: E501

        :param wait_host: The wait_host of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._wait_host = wait_host

    @property
    def wait_workload(self):
        """Gets the wait_workload of this SLAServiceStatusByJobs.  # noqa: E501

        Wait Workload  # noqa: E501

        :return: The wait_workload of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._wait_workload

    @wait_workload.setter
    def wait_workload(self, wait_workload):
        """Sets the wait_workload of this SLAServiceStatusByJobs.

        Wait Workload  # noqa: E501

        :param wait_workload: The wait_workload of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._wait_workload = wait_workload

    @property
    def completed(self):
        """Gets the completed of this SLAServiceStatusByJobs.  # noqa: E501

        Completed  # noqa: E501

        :return: The completed of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this SLAServiceStatusByJobs.

        Completed  # noqa: E501

        :param completed: The completed of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._completed = completed

    @property
    def error(self):
        """Gets the error of this SLAServiceStatusByJobs.  # noqa: E501

        Error  # noqa: E501

        :return: The error of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SLAServiceStatusByJobs.

        Error  # noqa: E501

        :param error: The error of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def unknown(self):
        """Gets the unknown of this SLAServiceStatusByJobs.  # noqa: E501

        Unkwown  # noqa: E501

        :return: The unknown of this SLAServiceStatusByJobs.  # noqa: E501
        :rtype: str
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this SLAServiceStatusByJobs.

        Unkwown  # noqa: E501

        :param unknown: The unknown of this SLAServiceStatusByJobs.  # noqa: E501
        :type: str
        """

        self._unknown = unknown

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
        if issubclass(SLAServiceStatusByJobs, dict):
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
        if not isinstance(other, SLAServiceStatusByJobs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SLAServiceStatusByJobs):
            return True

        return self.to_dict() != other.to_dict()
