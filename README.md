# solutioncatalog-api
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/mintproject/solution-catalog-python-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mintproject/solution-catalog-python-api-client.git`)

Then import the package:
```python
import solutioncatalog 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import solutioncatalog
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import solutioncatalog
from solutioncatalog.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://solution.mint.isi.edu/v0.0.1
configuration.host = "https://solution.mint.isi.edu/v0.0.1"
# Create an instance of the API class
api_instance = solutioncatalog.ResultsApi(solutioncatalog.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://solution.mint.isi.edu/v0.0.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ResultsApi* | [**results_scenario_id_subgoal_id_thread_id_get**](docs/endpoints/ResultsApi.md#results_scenario_id_subgoal_id_thread_id_get) | **GET** /results/{scenario_id}/{subgoal_id}/{thread_id} | Get the results of a thread


## Documentation For Models

 - [ProblemFormulation](docs/endpoints/ProblemFormulation.md)
 - [Scenario](docs/endpoints/Scenario.md)
 - [Thread](docs/endpoints/Thread.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




