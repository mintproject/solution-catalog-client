# solutioncatalog.ResultsApi

All URIs are relative to *https://solution.mint.isi.edu/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**results_scenario_id_subgoal_id_thread_id_get**](ResultsApi.md#results_scenario_id_subgoal_id_thread_id_get) | **GET** /results/{scenario_id}/{subgoal_id}/{thread_id} | Get the results of a thread


# **results_scenario_id_subgoal_id_thread_id_get**
> object results_scenario_id_subgoal_id_thread_id_get(scenario_id, subgoal_id, thread_id)

Get the results of a thread

Gets the details of a single instance of a results

### Example

```python
from __future__ import print_function
import time
import solutioncatalog
from solutioncatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = solutioncatalog.ResultsApi()
scenario_id = 'scenario_id_example' # str | The ID of the scenario
subgoal_id = 'subgoal_id_example' # str | The ID of the subgoal
thread_id = 'thread_id_example' # str | The ID of the thread

try:
    # Get the results of a thread
    api_response = api_instance.results_scenario_id_subgoal_id_thread_id_get(scenario_id, subgoal_id, thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->results_scenario_id_subgoal_id_thread_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| The ID of the scenario | 
 **subgoal_id** | **str**| The ID of the subgoal | 
 **thread_id** | **str**| The ID of the thread | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of the results of a thread |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

