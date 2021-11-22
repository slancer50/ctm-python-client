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


class OrderParameters(object):
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
        "create_duplicate": "bool",
        "hold": "bool",
        "ignore_criteria": "bool",
        "independent_flow": "bool",
        "order_date": "str",
        "order_into_folder": "str",
        "order_into_folder_order_id": "str",
        "variables": "list[NameValueAttribute]",
        "wait_for_order_date": "bool",
    }

    attribute_map = {
        "create_duplicate": "create_duplicate",
        "hold": "hold",
        "ignore_criteria": "ignore_criteria",
        "independent_flow": "independent_flow",
        "order_date": "order_date",
        "order_into_folder": "order_into_folder",
        "order_into_folder_order_id": "order_into_folder_order_id",
        "variables": "variables",
        "wait_for_order_date": "wait_for_order_date",
    }

    def __init__(
        self,
        create_duplicate=None,
        hold=None,
        ignore_criteria=None,
        independent_flow=None,
        order_date=None,
        order_into_folder=None,
        order_into_folder_order_id=None,
        variables=None,
        wait_for_order_date=None,
        _configuration=None,
    ):  # noqa: E501
        """OrderParameters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_duplicate = None
        self._hold = None
        self._ignore_criteria = None
        self._independent_flow = None
        self._order_date = None
        self._order_into_folder = None
        self._order_into_folder_order_id = None
        self._variables = None
        self._wait_for_order_date = None
        self.discriminator = None

        if create_duplicate is not None:
            self.create_duplicate = create_duplicate
        if hold is not None:
            self.hold = hold
        if ignore_criteria is not None:
            self.ignore_criteria = ignore_criteria
        if independent_flow is not None:
            self.independent_flow = independent_flow
        if order_date is not None:
            self.order_date = order_date
        if order_into_folder is not None:
            self.order_into_folder = order_into_folder
        if order_into_folder_order_id is not None:
            self.order_into_folder_order_id = order_into_folder_order_id
        if variables is not None:
            self.variables = variables
        if wait_for_order_date is not None:
            self.wait_for_order_date = wait_for_order_date

    @property
    def create_duplicate(self):
        """Gets the create_duplicate of this OrderParameters.  # noqa: E501


        :return: The create_duplicate of this OrderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._create_duplicate

    @create_duplicate.setter
    def create_duplicate(self, create_duplicate):
        """Sets the create_duplicate of this OrderParameters.


        :param create_duplicate: The create_duplicate of this OrderParameters.  # noqa: E501
        :type: bool
        """

        self._create_duplicate = create_duplicate

    @property
    def hold(self):
        """Gets the hold of this OrderParameters.  # noqa: E501


        :return: The hold of this OrderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._hold

    @hold.setter
    def hold(self, hold):
        """Sets the hold of this OrderParameters.


        :param hold: The hold of this OrderParameters.  # noqa: E501
        :type: bool
        """

        self._hold = hold

    @property
    def ignore_criteria(self):
        """Gets the ignore_criteria of this OrderParameters.  # noqa: E501


        :return: The ignore_criteria of this OrderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_criteria

    @ignore_criteria.setter
    def ignore_criteria(self, ignore_criteria):
        """Sets the ignore_criteria of this OrderParameters.


        :param ignore_criteria: The ignore_criteria of this OrderParameters.  # noqa: E501
        :type: bool
        """

        self._ignore_criteria = ignore_criteria

    @property
    def independent_flow(self):
        """Gets the independent_flow of this OrderParameters.  # noqa: E501


        :return: The independent_flow of this OrderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._independent_flow

    @independent_flow.setter
    def independent_flow(self, independent_flow):
        """Sets the independent_flow of this OrderParameters.


        :param independent_flow: The independent_flow of this OrderParameters.  # noqa: E501
        :type: bool
        """

        self._independent_flow = independent_flow

    @property
    def order_date(self):
        """Gets the order_date of this OrderParameters.  # noqa: E501


        :return: The order_date of this OrderParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this OrderParameters.


        :param order_date: The order_date of this OrderParameters.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def order_into_folder(self):
        """Gets the order_into_folder of this OrderParameters.  # noqa: E501


        :return: The order_into_folder of this OrderParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_into_folder

    @order_into_folder.setter
    def order_into_folder(self, order_into_folder):
        """Sets the order_into_folder of this OrderParameters.


        :param order_into_folder: The order_into_folder of this OrderParameters.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "New",
            "Recent",
            "OrderId",
            "Alone",
            "UNRECOGNIZED",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and order_into_folder not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `order_into_folder` ({0}), must be one of {1}".format(  # noqa: E501
                    order_into_folder, allowed_values
                )
            )

        self._order_into_folder = order_into_folder

    @property
    def order_into_folder_order_id(self):
        """Gets the order_into_folder_order_id of this OrderParameters.  # noqa: E501


        :return: The order_into_folder_order_id of this OrderParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_into_folder_order_id

    @order_into_folder_order_id.setter
    def order_into_folder_order_id(self, order_into_folder_order_id):
        """Sets the order_into_folder_order_id of this OrderParameters.


        :param order_into_folder_order_id: The order_into_folder_order_id of this OrderParameters.  # noqa: E501
        :type: str
        """

        self._order_into_folder_order_id = order_into_folder_order_id

    @property
    def variables(self):
        """Gets the variables of this OrderParameters.  # noqa: E501


        :return: The variables of this OrderParameters.  # noqa: E501
        :rtype: list[NameValueAttribute]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this OrderParameters.


        :param variables: The variables of this OrderParameters.  # noqa: E501
        :type: list[NameValueAttribute]
        """

        self._variables = variables

    @property
    def wait_for_order_date(self):
        """Gets the wait_for_order_date of this OrderParameters.  # noqa: E501


        :return: The wait_for_order_date of this OrderParameters.  # noqa: E501
        :rtype: bool
        """
        return self._wait_for_order_date

    @wait_for_order_date.setter
    def wait_for_order_date(self, wait_for_order_date):
        """Sets the wait_for_order_date of this OrderParameters.


        :param wait_for_order_date: The wait_for_order_date of this OrderParameters.  # noqa: E501
        :type: bool
        """

        self._wait_for_order_date = wait_for_order_date

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
        if issubclass(OrderParameters, dict):
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
        if not isinstance(other, OrderParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderParameters):
            return True

        return self.to_dict() != other.to_dict()
