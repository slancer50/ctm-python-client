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


class CommunicationAnalysisResponseType(object):
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
        "basic_info": "CtmagentBasicInfoType",
        "ctmagent_ctm_tests_type": "list[CtmagentCtmTestType]",
        "ctmagent_states_changed_type": "list[CtmagentStateChangedType]",
    }

    attribute_map = {
        "basic_info": "basicInfo",
        "ctmagent_ctm_tests_type": "ctmagentCtmTestsType",
        "ctmagent_states_changed_type": "ctmagentStatesChangedType",
    }

    def __init__(
        self,
        basic_info=None,
        ctmagent_ctm_tests_type=None,
        ctmagent_states_changed_type=None,
        _configuration=None,
    ):  # noqa: E501
        """CommunicationAnalysisResponseType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._basic_info = None
        self._ctmagent_ctm_tests_type = None
        self._ctmagent_states_changed_type = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if ctmagent_ctm_tests_type is not None:
            self.ctmagent_ctm_tests_type = ctmagent_ctm_tests_type
        if ctmagent_states_changed_type is not None:
            self.ctmagent_states_changed_type = ctmagent_states_changed_type

    @property
    def basic_info(self):
        """Gets the basic_info of this CommunicationAnalysisResponseType.  # noqa: E501

        The basic information pat of the report  # noqa: E501

        :return: The basic_info of this CommunicationAnalysisResponseType.  # noqa: E501
        :rtype: CtmagentBasicInfoType
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this CommunicationAnalysisResponseType.

        The basic information pat of the report  # noqa: E501

        :param basic_info: The basic_info of this CommunicationAnalysisResponseType.  # noqa: E501
        :type: CtmagentBasicInfoType
        """

        self._basic_info = basic_info

    @property
    def ctmagent_ctm_tests_type(self):
        """Gets the ctmagent_ctm_tests_type of this CommunicationAnalysisResponseType.  # noqa: E501

        The list of 4 tests executed and their output  # noqa: E501

        :return: The ctmagent_ctm_tests_type of this CommunicationAnalysisResponseType.  # noqa: E501
        :rtype: list[CtmagentCtmTestType]
        """
        return self._ctmagent_ctm_tests_type

    @ctmagent_ctm_tests_type.setter
    def ctmagent_ctm_tests_type(self, ctmagent_ctm_tests_type):
        """Sets the ctmagent_ctm_tests_type of this CommunicationAnalysisResponseType.

        The list of 4 tests executed and their output  # noqa: E501

        :param ctmagent_ctm_tests_type: The ctmagent_ctm_tests_type of this CommunicationAnalysisResponseType.  # noqa: E501
        :type: list[CtmagentCtmTestType]
        """

        self._ctmagent_ctm_tests_type = ctmagent_ctm_tests_type

    @property
    def ctmagent_states_changed_type(self):
        """Gets the ctmagent_states_changed_type of this CommunicationAnalysisResponseType.  # noqa: E501

        The list of 10 latest Agent's state changed to Unavailable and timestamp  # noqa: E501

        :return: The ctmagent_states_changed_type of this CommunicationAnalysisResponseType.  # noqa: E501
        :rtype: list[CtmagentStateChangedType]
        """
        return self._ctmagent_states_changed_type

    @ctmagent_states_changed_type.setter
    def ctmagent_states_changed_type(self, ctmagent_states_changed_type):
        """Sets the ctmagent_states_changed_type of this CommunicationAnalysisResponseType.

        The list of 10 latest Agent's state changed to Unavailable and timestamp  # noqa: E501

        :param ctmagent_states_changed_type: The ctmagent_states_changed_type of this CommunicationAnalysisResponseType.  # noqa: E501
        :type: list[CtmagentStateChangedType]
        """

        self._ctmagent_states_changed_type = ctmagent_states_changed_type

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
        if issubclass(CommunicationAnalysisResponseType, dict):
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
        if not isinstance(other, CommunicationAnalysisResponseType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommunicationAnalysisResponseType):
            return True

        return self.to_dict() != other.to_dict()
