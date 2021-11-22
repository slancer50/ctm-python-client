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


class ComponentMetaDataProperties(object):
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
        "display_name": "str",
        "display_name_id": "str",
        "name": "str",
        "sections": "list[SectionMetadataProperties]",
    }

    attribute_map = {
        "display_name": "displayName",
        "display_name_id": "displayNameID",
        "name": "name",
        "sections": "sections",
    }

    def __init__(
        self,
        display_name=None,
        display_name_id=None,
        name=None,
        sections=None,
        _configuration=None,
    ):  # noqa: E501
        """ComponentMetaDataProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._display_name_id = None
        self._name = None
        self._sections = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if display_name_id is not None:
            self.display_name_id = display_name_id
        if name is not None:
            self.name = name
        if sections is not None:
            self.sections = sections

    @property
    def display_name(self):
        """Gets the display_name of this ComponentMetaDataProperties.  # noqa: E501


        :return: The display_name of this ComponentMetaDataProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ComponentMetaDataProperties.


        :param display_name: The display_name of this ComponentMetaDataProperties.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_name_id(self):
        """Gets the display_name_id of this ComponentMetaDataProperties.  # noqa: E501


        :return: The display_name_id of this ComponentMetaDataProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name_id

    @display_name_id.setter
    def display_name_id(self, display_name_id):
        """Sets the display_name_id of this ComponentMetaDataProperties.


        :param display_name_id: The display_name_id of this ComponentMetaDataProperties.  # noqa: E501
        :type: str
        """

        self._display_name_id = display_name_id

    @property
    def name(self):
        """Gets the name of this ComponentMetaDataProperties.  # noqa: E501


        :return: The name of this ComponentMetaDataProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentMetaDataProperties.


        :param name: The name of this ComponentMetaDataProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sections(self):
        """Gets the sections of this ComponentMetaDataProperties.  # noqa: E501


        :return: The sections of this ComponentMetaDataProperties.  # noqa: E501
        :rtype: list[SectionMetadataProperties]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this ComponentMetaDataProperties.


        :param sections: The sections of this ComponentMetaDataProperties.  # noqa: E501
        :type: list[SectionMetadataProperties]
        """

        self._sections = sections

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
        if issubclass(ComponentMetaDataProperties, dict):
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
        if not isinstance(other, ComponentMetaDataProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentMetaDataProperties):
            return True

        return self.to_dict() != other.to_dict()
