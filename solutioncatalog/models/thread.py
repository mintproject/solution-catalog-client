# coding: utf-8

"""
    Solution Catalog

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Thread(object):
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
        'text': 'object',
        'time_period': 'object',
        'indicators': 'object',
        'models': 'object',
        'datasets': 'object',
        'results': 'object'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'time_period': 'time_period',
        'indicators': 'indicators',
        'models': 'models',
        'datasets': 'datasets',
        'results': 'results'
    }

    def __init__(self, id=None, text=None, time_period=None, indicators=None, models=None, datasets=None, results=None):  # noqa: E501
        """Thread - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._text = None
        self._time_period = None
        self._indicators = None
        self._models = None
        self._datasets = None
        self._results = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if time_period is not None:
            self.time_period = time_period
        if indicators is not None:
            self.indicators = indicators
        if models is not None:
            self.models = models
        if datasets is not None:
            self.datasets = datasets
        if results is not None:
            self.results = results

    @property
    def id(self):
        """Gets the id of this Thread.  # noqa: E501


        :return: The id of this Thread.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Thread.


        :param id: The id of this Thread.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Thread.  # noqa: E501


        :return: The text of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Thread.


        :param text: The text of this Thread.  # noqa: E501
        :type: object
        """

        self._text = text

    @property
    def time_period(self):
        """Gets the time_period of this Thread.  # noqa: E501


        :return: The time_period of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this Thread.


        :param time_period: The time_period of this Thread.  # noqa: E501
        :type: object
        """

        self._time_period = time_period

    @property
    def indicators(self):
        """Gets the indicators of this Thread.  # noqa: E501


        :return: The indicators of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this Thread.


        :param indicators: The indicators of this Thread.  # noqa: E501
        :type: object
        """

        self._indicators = indicators

    @property
    def models(self):
        """Gets the models of this Thread.  # noqa: E501


        :return: The models of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this Thread.


        :param models: The models of this Thread.  # noqa: E501
        :type: object
        """

        self._models = models

    @property
    def datasets(self):
        """Gets the datasets of this Thread.  # noqa: E501


        :return: The datasets of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this Thread.


        :param datasets: The datasets of this Thread.  # noqa: E501
        :type: object
        """

        self._datasets = datasets

    @property
    def results(self):
        """Gets the results of this Thread.  # noqa: E501


        :return: The results of this Thread.  # noqa: E501
        :rtype: object
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Thread.


        :param results: The results of this Thread.  # noqa: E501
        :type: object
        """

        self._results = results

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
        if not isinstance(other, Thread):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
