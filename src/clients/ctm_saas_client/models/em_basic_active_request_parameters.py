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


class EMBasicActiveRequestParameters(object):
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
        'annotation_category': 'str',
        'annotation_notes': 'str',
        'ctm_name': 'str',
        'net_name': 'str'
    }

    attribute_map = {
        'annotation_category': 'annotation_category',
        'annotation_notes': 'annotation_notes',
        'ctm_name': 'ctm_name',
        'net_name': 'net_name'
    }

    def __init__(self, annotation_category=None, annotation_notes=None, ctm_name=None, net_name=None, _configuration=None):  # noqa: E501
        """EMBasicActiveRequestParameters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotation_category = None
        self._annotation_notes = None
        self._ctm_name = None
        self._net_name = None
        self.discriminator = None

        if annotation_category is not None:
            self.annotation_category = annotation_category
        if annotation_notes is not None:
            self.annotation_notes = annotation_notes
        if ctm_name is not None:
            self.ctm_name = ctm_name
        if net_name is not None:
            self.net_name = net_name

    @property
    def annotation_category(self):
        """Gets the annotation_category of this EMBasicActiveRequestParameters.  # noqa: E501


        :return: The annotation_category of this EMBasicActiveRequestParameters.  # noqa: E501
        :rtype: str
        """
        return self._annotation_category

    @annotation_category.setter
    def annotation_category(self, annotation_category):
        """Sets the annotation_category of this EMBasicActiveRequestParameters.


        :param annotation_category: The annotation_category of this EMBasicActiveRequestParameters.  # noqa: E501
        :type: str
        """

        self._annotation_category = annotation_category

    @property
    def annotation_notes(self):
        """Gets the annotation_notes of this EMBasicActiveRequestParameters.  # noqa: E501


        :return: The annotation_notes of this EMBasicActiveRequestParameters.  # noqa: E501
        :rtype: str
        """
        return self._annotation_notes

    @annotation_notes.setter
    def annotation_notes(self, annotation_notes):
        """Sets the annotation_notes of this EMBasicActiveRequestParameters.


        :param annotation_notes: The annotation_notes of this EMBasicActiveRequestParameters.  # noqa: E501
        :type: str
        """

        self._annotation_notes = annotation_notes

    @property
    def ctm_name(self):
        """Gets the ctm_name of this EMBasicActiveRequestParameters.  # noqa: E501


        :return: The ctm_name of this EMBasicActiveRequestParameters.  # noqa: E501
        :rtype: str
        """
        return self._ctm_name

    @ctm_name.setter
    def ctm_name(self, ctm_name):
        """Sets the ctm_name of this EMBasicActiveRequestParameters.


        :param ctm_name: The ctm_name of this EMBasicActiveRequestParameters.  # noqa: E501
        :type: str
        """

        self._ctm_name = ctm_name

    @property
    def net_name(self):
        """Gets the net_name of this EMBasicActiveRequestParameters.  # noqa: E501


        :return: The net_name of this EMBasicActiveRequestParameters.  # noqa: E501
        :rtype: str
        """
        return self._net_name

    @net_name.setter
    def net_name(self, net_name):
        """Sets the net_name of this EMBasicActiveRequestParameters.


        :param net_name: The net_name of this EMBasicActiveRequestParameters.  # noqa: E501
        :type: str
        """

        self._net_name = net_name

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
        if issubclass(EMBasicActiveRequestParameters, dict):
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
        if not isinstance(other, EMBasicActiveRequestParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EMBasicActiveRequestParameters):
            return True

        return self.to_dict() != other.to_dict()
