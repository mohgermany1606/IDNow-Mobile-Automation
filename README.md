# IDNow API Automation 

This project is a Python-based test framework using the unittest module to test API endpoints. It specifically tests the browser support matrix for the autoident key in the API response.

## Prerequisites

- Python 3.x
- 'requests' library
-  'pytest' library
- 'jsonschema' library

## Installation

1. Clone this repository to your local machine:

   git clone https://github.com/mohgermany1606/IDNow-Mobile-Automation.git
   cd api_test_framework

2. python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install the dependencies
 pip install -r requirements.txt

# Files

**requirements.txt**
This file contains the list of dependencies required for the project:
1. requests
2. pytest
3. jsonschema


**config/config.py**
It contains BASE URL which is used in base_test.py

**tests/test_api.py**
The test case test_autoident_browser_support checks if the autoident key exists and verifies that the min key is present for every browser in the browserSupportMatrix.


**utils/base_test.py**
It provides an'APIClient' class for making HTTP Requests.It includes methods for making GET, POST, PUT, and DELETE requests to the API

It has below class methods - 

**setUpClass(cls)**: Sets up the test case, including the base URL and a session.

**tearDownClass(cls)**: Tears down the test case, closing the session.

**get(self, url, params=None)**: Performs a GET request.

**post(self, url, data=None, json=None)**: Performs a POST request.

**put(self, url, data=None, json=None)**: Performs a PUT request.

**delete(self, url)**: Performs a DELETE request.

**check_min_key_exists(self, browser_dict)**: Checks whether the 'min' key exists for every browser in the given dictionary.


**requirements.txt**
This file contains the list of dependencies required for the project:
requests
pytest
jsonschema

 **Run Test -**
Test can be run using command pytest -s





