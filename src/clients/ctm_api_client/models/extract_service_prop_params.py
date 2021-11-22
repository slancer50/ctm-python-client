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


class ExtractServicePropParams(object):
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
        "option": "str",
        "ruletable": "str",
        "aidbglvl": "str",
        "filter": "str",
        "exitpgm": "str",
        "aitout": "str",
        "aistatus": "str",
    }

    attribute_map = {
        "option": "option",
        "ruletable": "ruletable",
        "aidbglvl": "aidbglvl",
        "filter": "filter",
        "exitpgm": "exitpgm",
        "aitout": "aitout",
        "aistatus": "aistatus",
    }

    def __init__(
        self,
        option=None,
        ruletable=None,
        aidbglvl=None,
        filter=None,
        exitpgm=None,
        aitout=None,
        aistatus=None,
        _configuration=None,
    ):  # noqa: E501
        """ExtractServicePropParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._option = None
        self._ruletable = None
        self._aidbglvl = None
        self._filter = None
        self._exitpgm = None
        self._aitout = None
        self._aistatus = None
        self.discriminator = None

        if option is not None:
            self.option = option
        if ruletable is not None:
            self.ruletable = ruletable
        if aidbglvl is not None:
            self.aidbglvl = aidbglvl
        if filter is not None:
            self.filter = filter
        if exitpgm is not None:
            self.exitpgm = exitpgm
        if aitout is not None:
            self.aitout = aitout
        if aistatus is not None:
            self.aistatus = aistatus

    @property
    def option(self):
        """Gets the option of this ExtractServicePropParams.  # noqa: E501

        Start with Agent startup  # noqa: E501

        :return: The option of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ExtractServicePropParams.

        Start with Agent startup  # noqa: E501

        :param option: The option of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._option = option

    @property
    def ruletable(self):
        """Gets the ruletable of this ExtractServicePropParams.  # noqa: E501

        Rule table name  # noqa: E501

        :return: The ruletable of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._ruletable

    @ruletable.setter
    def ruletable(self, ruletable):
        """Sets the ruletable of this ExtractServicePropParams.

        Rule table name  # noqa: E501

        :param ruletable: The ruletable of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._ruletable = ruletable

    @property
    def aidbglvl(self):
        """Gets the aidbglvl of this ExtractServicePropParams.  # noqa: E501

        Extractor Diagnostic Level  # noqa: E501

        :return: The aidbglvl of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._aidbglvl

    @aidbglvl.setter
    def aidbglvl(self, aidbglvl):
        """Sets the aidbglvl of this ExtractServicePropParams.

        Extractor Diagnostic Level  # noqa: E501

        :param aidbglvl: The aidbglvl of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._aidbglvl = aidbglvl

    @property
    def filter(self):
        """Gets the filter of this ExtractServicePropParams.  # noqa: E501

        Filter Key  # noqa: E501

        :return: The filter of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ExtractServicePropParams.

        Filter Key  # noqa: E501

        :param filter: The filter of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def exitpgm(self):
        """Gets the exitpgm of this ExtractServicePropParams.  # noqa: E501

        Exit Program Name  # noqa: E501

        :return: The exitpgm of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._exitpgm

    @exitpgm.setter
    def exitpgm(self, exitpgm):
        """Sets the exitpgm of this ExtractServicePropParams.

        Exit Program Name  # noqa: E501

        :param exitpgm: The exitpgm of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._exitpgm = exitpgm

    @property
    def aitout(self):
        """Gets the aitout of this ExtractServicePropParams.  # noqa: E501

        Extractor Timeout  # noqa: E501

        :return: The aitout of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._aitout

    @aitout.setter
    def aitout(self, aitout):
        """Sets the aitout of this ExtractServicePropParams.

        Extractor Timeout  # noqa: E501

        :param aitout: The aitout of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._aitout = aitout

    @property
    def aistatus(self):
        """Gets the aistatus of this ExtractServicePropParams.  # noqa: E501

        Service Status  # noqa: E501

        :return: The aistatus of this ExtractServicePropParams.  # noqa: E501
        :rtype: str
        """
        return self._aistatus

    @aistatus.setter
    def aistatus(self, aistatus):
        """Sets the aistatus of this ExtractServicePropParams.

        Service Status  # noqa: E501

        :param aistatus: The aistatus of this ExtractServicePropParams.  # noqa: E501
        :type: str
        """

        self._aistatus = aistatus

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
        if issubclass(ExtractServicePropParams, dict):
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
        if not isinstance(other, ExtractServicePropParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtractServicePropParams):
            return True

        return self.to_dict() != other.to_dict()
