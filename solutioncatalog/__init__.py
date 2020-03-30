# coding: utf-8

# flake8: noqa

"""
    Solution Catalog

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.1"

# import apis into sdk package
from solutioncatalog.api.results_api import ResultsApi

# import ApiClient
from solutioncatalog.api_client import ApiClient
from solutioncatalog.configuration import Configuration
from solutioncatalog.exceptions import OpenApiException
from solutioncatalog.exceptions import ApiTypeError
from solutioncatalog.exceptions import ApiValueError
from solutioncatalog.exceptions import ApiKeyError
from solutioncatalog.exceptions import ApiException
# import models into sdk package
from solutioncatalog.models.problem_formulation import ProblemFormulation
from solutioncatalog.models.scenario import Scenario
from solutioncatalog.models.thread import Thread
