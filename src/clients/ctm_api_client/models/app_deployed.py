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


class AppDeployed(object):
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
        "displayname": "str",
        "name": "str",
        "version": "str",
        "default_type": "str",
        "last_deployed": "str",
        "last_published": "str",
        "icon_base64": "str",
        "created_on": "str",
        "created_by": "str",
    }

    attribute_map = {
        "displayname": "displayname",
        "name": "name",
        "version": "version",
        "default_type": "defaultType",
        "last_deployed": "lastDeployed",
        "last_published": "lastPublished",
        "icon_base64": "iconBase64",
        "created_on": "createdOn",
        "created_by": "createdBy",
    }

    def __init__(
        self,
        displayname=None,
        name=None,
        version=None,
        default_type=None,
        last_deployed=None,
        last_published=None,
        icon_base64=None,
        created_on=None,
        created_by=None,
        _configuration=None,
    ):  # noqa: E501
        """AppDeployed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._displayname = None
        self._name = None
        self._version = None
        self._default_type = None
        self._last_deployed = None
        self._last_published = None
        self._icon_base64 = None
        self._created_on = None
        self._created_by = None
        self.discriminator = None

        if displayname is not None:
            self.displayname = displayname
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if default_type is not None:
            self.default_type = default_type
        if last_deployed is not None:
            self.last_deployed = last_deployed
        if last_published is not None:
            self.last_published = last_published
        if icon_base64 is not None:
            self.icon_base64 = icon_base64
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by

    @property
    def displayname(self):
        """Gets the displayname of this AppDeployed.  # noqa: E501

        job type display name  # noqa: E501

        :return: The displayname of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this AppDeployed.

        job type display name  # noqa: E501

        :param displayname: The displayname of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def name(self):
        """Gets the name of this AppDeployed.  # noqa: E501

        job type name  # noqa: E501

        :return: The name of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppDeployed.

        job type name  # noqa: E501

        :param name: The name of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this AppDeployed.  # noqa: E501

        version  # noqa: E501

        :return: The version of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppDeployed.

        version  # noqa: E501

        :param version: The version of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def default_type(self):
        """Gets the default_type of this AppDeployed.  # noqa: E501

        default type  # noqa: E501

        :return: The default_type of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._default_type

    @default_type.setter
    def default_type(self, default_type):
        """Sets the default_type of this AppDeployed.

        default type  # noqa: E501

        :param default_type: The default_type of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._default_type = default_type

    @property
    def last_deployed(self):
        """Gets the last_deployed of this AppDeployed.  # noqa: E501

        last deployment date  # noqa: E501

        :return: The last_deployed of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._last_deployed

    @last_deployed.setter
    def last_deployed(self, last_deployed):
        """Sets the last_deployed of this AppDeployed.

        last deployment date  # noqa: E501

        :param last_deployed: The last_deployed of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._last_deployed = last_deployed

    @property
    def last_published(self):
        """Gets the last_published of this AppDeployed.  # noqa: E501

        last publishment date  # noqa: E501

        :return: The last_published of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._last_published

    @last_published.setter
    def last_published(self, last_published):
        """Sets the last_published of this AppDeployed.

        last publishment date  # noqa: E501

        :param last_published: The last_published of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._last_published = last_published

    @property
    def icon_base64(self):
        """Gets the icon_base64 of this AppDeployed.  # noqa: E501

        base64 icon job  # noqa: E501

        :return: The icon_base64 of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._icon_base64

    @icon_base64.setter
    def icon_base64(self, icon_base64):
        """Sets the icon_base64 of this AppDeployed.

        base64 icon job  # noqa: E501

        :param icon_base64: The icon_base64 of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._icon_base64 = icon_base64

    @property
    def created_on(self):
        """Gets the created_on of this AppDeployed.  # noqa: E501

        creation date  # noqa: E501

        :return: The created_on of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AppDeployed.

        creation date  # noqa: E501

        :param created_on: The created_on of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this AppDeployed.  # noqa: E501

        creation author  # noqa: E501

        :return: The created_by of this AppDeployed.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AppDeployed.

        creation author  # noqa: E501

        :param created_by: The created_by of this AppDeployed.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(AppDeployed, dict):
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
        if not isinstance(other, AppDeployed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppDeployed):
            return True

        return self.to_dict() != other.to_dict()
