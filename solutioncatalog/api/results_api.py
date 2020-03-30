# coding: utf-8

"""
    Solution Catalog

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from solutioncatalog.api_client import ApiClient
from solutioncatalog.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ResultsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def results_scenario_id_subgoal_id_thread_id_get(self, scenario_id, subgoal_id, thread_id, **kwargs):  # noqa: E501
        """Get the results of a thread  # noqa: E501

        Gets the details of a single instance of a results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_scenario_id_subgoal_id_thread_id_get(scenario_id, subgoal_id, thread_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: The ID of the scenario (required)
        :param str subgoal_id: The ID of the subgoal (required)
        :param str thread_id: The ID of the thread (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.results_scenario_id_subgoal_id_thread_id_get_with_http_info(scenario_id, subgoal_id, thread_id, **kwargs)  # noqa: E501

    def results_scenario_id_subgoal_id_thread_id_get_with_http_info(self, scenario_id, subgoal_id, thread_id, **kwargs):  # noqa: E501
        """Get the results of a thread  # noqa: E501

        Gets the details of a single instance of a results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_scenario_id_subgoal_id_thread_id_get_with_http_info(scenario_id, subgoal_id, thread_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: The ID of the scenario (required)
        :param str subgoal_id: The ID of the subgoal (required)
        :param str thread_id: The ID of the thread (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scenario_id', 'subgoal_id', 'thread_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_scenario_id_subgoal_id_thread_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if ('scenario_id' not in local_var_params or
                local_var_params['scenario_id'] is None):
            raise ApiValueError("Missing the required parameter `scenario_id` when calling `results_scenario_id_subgoal_id_thread_id_get`")  # noqa: E501
        # verify the required parameter 'subgoal_id' is set
        if ('subgoal_id' not in local_var_params or
                local_var_params['subgoal_id'] is None):
            raise ApiValueError("Missing the required parameter `subgoal_id` when calling `results_scenario_id_subgoal_id_thread_id_get`")  # noqa: E501
        # verify the required parameter 'thread_id' is set
        if ('thread_id' not in local_var_params or
                local_var_params['thread_id'] is None):
            raise ApiValueError("Missing the required parameter `thread_id` when calling `results_scenario_id_subgoal_id_thread_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scenario_id' in local_var_params:
            path_params['scenario_id'] = local_var_params['scenario_id']  # noqa: E501
        if 'subgoal_id' in local_var_params:
            path_params['subgoal_id'] = local_var_params['subgoal_id']  # noqa: E501
        if 'thread_id' in local_var_params:
            path_params['thread_id'] = local_var_params['thread_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/results/{scenario_id}/{subgoal_id}/{thread_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
