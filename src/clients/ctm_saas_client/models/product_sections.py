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


class ProductSections(object):
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
        'sections': 'list[ProductDescription]',
        'product_description_url': 'str'
    }

    attribute_map = {
        'sections': 'sections',
        'product_description_url': 'productDescriptionUrl'
    }

    def __init__(self, sections=None, product_description_url=None, _configuration=None):  # noqa: E501
        """ProductSections - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sections = None
        self._product_description_url = None
        self.discriminator = None

        if sections is not None:
            self.sections = sections
        if product_description_url is not None:
            self.product_description_url = product_description_url

    @property
    def sections(self):
        """Gets the sections of this ProductSections.  # noqa: E501


        :return: The sections of this ProductSections.  # noqa: E501
        :rtype: list[ProductDescription]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this ProductSections.


        :param sections: The sections of this ProductSections.  # noqa: E501
        :type: list[ProductDescription]
        """

        self._sections = sections

    @property
    def product_description_url(self):
        """Gets the product_description_url of this ProductSections.  # noqa: E501

        The product description. HIDDEN  # noqa: E501

        :return: The product_description_url of this ProductSections.  # noqa: E501
        :rtype: str
        """
        return self._product_description_url

    @product_description_url.setter
    def product_description_url(self, product_description_url):
        """Sets the product_description_url of this ProductSections.

        The product description. HIDDEN  # noqa: E501

        :param product_description_url: The product_description_url of this ProductSections.  # noqa: E501
        :type: str
        """

        self._product_description_url = product_description_url

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
        if issubclass(ProductSections, dict):
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
        if not isinstance(other, ProductSections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSections):
            return True

        return self.to_dict() != other.to_dict()
