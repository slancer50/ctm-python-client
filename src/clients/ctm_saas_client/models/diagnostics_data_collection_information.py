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


class DiagnosticsDataCollectionInformation(object):
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
        'usage_measurements': 'bool',
        'logs_and_configuration': 'bool',
        'days': 'int',
        'save_to': 'str',
        'cmd_params': 'str'
    }

    attribute_map = {
        'usage_measurements': 'usageMeasurements',
        'logs_and_configuration': 'logsAndConfiguration',
        'days': 'days',
        'save_to': 'saveTo',
        'cmd_params': 'cmdParams'
    }

    def __init__(self, usage_measurements=None, logs_and_configuration=None, days=None, save_to=None, cmd_params=None, _configuration=None):  # noqa: E501
        """DiagnosticsDataCollectionInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._usage_measurements = None
        self._logs_and_configuration = None
        self._days = None
        self._save_to = None
        self._cmd_params = None
        self.discriminator = None

        if usage_measurements is not None:
            self.usage_measurements = usage_measurements
        if logs_and_configuration is not None:
            self.logs_and_configuration = logs_and_configuration
        if days is not None:
            self.days = days
        if save_to is not None:
            self.save_to = save_to
        if cmd_params is not None:
            self.cmd_params = cmd_params

    @property
    def usage_measurements(self):
        """Gets the usage_measurements of this DiagnosticsDataCollectionInformation.  # noqa: E501

        Collect usage measurements HIDDEN  # noqa: E501

        :return: The usage_measurements of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :rtype: bool
        """
        return self._usage_measurements

    @usage_measurements.setter
    def usage_measurements(self, usage_measurements):
        """Sets the usage_measurements of this DiagnosticsDataCollectionInformation.

        Collect usage measurements HIDDEN  # noqa: E501

        :param usage_measurements: The usage_measurements of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :type: bool
        """

        self._usage_measurements = usage_measurements

    @property
    def logs_and_configuration(self):
        """Gets the logs_and_configuration of this DiagnosticsDataCollectionInformation.  # noqa: E501

        Collect logs and configuration HIDDEN  # noqa: E501

        :return: The logs_and_configuration of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :rtype: bool
        """
        return self._logs_and_configuration

    @logs_and_configuration.setter
    def logs_and_configuration(self, logs_and_configuration):
        """Sets the logs_and_configuration of this DiagnosticsDataCollectionInformation.

        Collect logs and configuration HIDDEN  # noqa: E501

        :param logs_and_configuration: The logs_and_configuration of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :type: bool
        """

        self._logs_and_configuration = logs_and_configuration

    @property
    def days(self):
        """Gets the days of this DiagnosticsDataCollectionInformation.  # noqa: E501

        Number of days HIDDEN  # noqa: E501

        :return: The days of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this DiagnosticsDataCollectionInformation.

        Number of days HIDDEN  # noqa: E501

        :param days: The days of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def save_to(self):
        """Gets the save_to of this DiagnosticsDataCollectionInformation.  # noqa: E501

        Save to location HIDDEN  # noqa: E501

        :return: The save_to of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :rtype: str
        """
        return self._save_to

    @save_to.setter
    def save_to(self, save_to):
        """Sets the save_to of this DiagnosticsDataCollectionInformation.

        Save to location HIDDEN  # noqa: E501

        :param save_to: The save_to of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :type: str
        """

        self._save_to = save_to

    @property
    def cmd_params(self):
        """Gets the cmd_params of this DiagnosticsDataCollectionInformation.  # noqa: E501

        The command line parameters HIDDEN  # noqa: E501

        :return: The cmd_params of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :rtype: str
        """
        return self._cmd_params

    @cmd_params.setter
    def cmd_params(self, cmd_params):
        """Sets the cmd_params of this DiagnosticsDataCollectionInformation.

        The command line parameters HIDDEN  # noqa: E501

        :param cmd_params: The cmd_params of this DiagnosticsDataCollectionInformation.  # noqa: E501
        :type: str
        """

        self._cmd_params = cmd_params

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
        if issubclass(DiagnosticsDataCollectionInformation, dict):
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
        if not isinstance(other, DiagnosticsDataCollectionInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiagnosticsDataCollectionInformation):
            return True

        return self.to_dict() != other.to_dict()
