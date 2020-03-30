# coding: utf-8

"""
    Solution Catalog

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProblemFormulation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'text': 'str',
        'region': 'str',
        'subregion': 'str',
        'time_period': 'object'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'region': 'region',
        'subregion': 'subregion',
        'time_period': 'time_period'
    }

    def __init__(self, id=None, text=None, region=None, subregion=None, time_period=None):  # noqa: E501
        """ProblemFormulation - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._text = None
        self._region = None
        self._subregion = None
        self._time_period = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if region is not None:
            self.region = region
        if subregion is not None:
            self.subregion = subregion
        if time_period is not None:
            self.time_period = time_period

    @property
    def id(self):
        """Gets the id of this ProblemFormulation.  # noqa: E501


        :return: The id of this ProblemFormulation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProblemFormulation.


        :param id: The id of this ProblemFormulation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this ProblemFormulation.  # noqa: E501


        :return: The text of this ProblemFormulation.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ProblemFormulation.


        :param text: The text of this ProblemFormulation.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def region(self):
        """Gets the region of this ProblemFormulation.  # noqa: E501


        :return: The region of this ProblemFormulation.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ProblemFormulation.


        :param region: The region of this ProblemFormulation.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def subregion(self):
        """Gets the subregion of this ProblemFormulation.  # noqa: E501


        :return: The subregion of this ProblemFormulation.  # noqa: E501
        :rtype: str
        """
        return self._subregion

    @subregion.setter
    def subregion(self, subregion):
        """Sets the subregion of this ProblemFormulation.


        :param subregion: The subregion of this ProblemFormulation.  # noqa: E501
        :type: str
        """

        self._subregion = subregion

    @property
    def time_period(self):
        """Gets the time_period of this ProblemFormulation.  # noqa: E501


        :return: The time_period of this ProblemFormulation.  # noqa: E501
        :rtype: object
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this ProblemFormulation.


        :param time_period: The time_period of this ProblemFormulation.  # noqa: E501
        :type: object
        """

        self._time_period = time_period

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProblemFormulation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other