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


class DeployJobtypeResponse(object):
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
        "deployment_file": "str",
        "successful_deploys": "list[JobtypeAgent]",
    }

    attribute_map = {
        "deployment_file": "deploymentFile",
        "successful_deploys": "successfulDeploys",
    }

    def __init__(
        self, deployment_file=None, successful_deploys=None, _configuration=None
    ):  # noqa: E501
        """DeployJobtypeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deployment_file = None
        self._successful_deploys = None
        self.discriminator = None

        if deployment_file is not None:
            self.deployment_file = deployment_file
        if successful_deploys is not None:
            self.successful_deploys = successful_deploys

    @property
    def deployment_file(self):
        """Gets the deployment_file of this DeployJobtypeResponse.  # noqa: E501

        The name of the deployed .ctmai file  # noqa: E501

        :return: The deployment_file of this DeployJobtypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._deployment_file

    @deployment_file.setter
    def deployment_file(self, deployment_file):
        """Sets the deployment_file of this DeployJobtypeResponse.

        The name of the deployed .ctmai file  # noqa: E501

        :param deployment_file: The deployment_file of this DeployJobtypeResponse.  # noqa: E501
        :type: str
        """

        self._deployment_file = deployment_file

    @property
    def successful_deploys(self):
        """Gets the successful_deploys of this DeployJobtypeResponse.  # noqa: E501


        :return: The successful_deploys of this DeployJobtypeResponse.  # noqa: E501
        :rtype: list[JobtypeAgent]
        """
        return self._successful_deploys

    @successful_deploys.setter
    def successful_deploys(self, successful_deploys):
        """Sets the successful_deploys of this DeployJobtypeResponse.


        :param successful_deploys: The successful_deploys of this DeployJobtypeResponse.  # noqa: E501
        :type: list[JobtypeAgent]
        """

        self._successful_deploys = successful_deploys

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
        if issubclass(DeployJobtypeResponse, dict):
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
        if not isinstance(other, DeployJobtypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeployJobtypeResponse):
            return True

        return self.to_dict() != other.to_dict()
