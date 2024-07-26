# IDNow API Automation 

This project is a Python-based test framework using the unittest module to test API endpoints. It specifically tests the browser support matrix for the autoident key in the API response.

## Prerequisites

- Python 3.x
- 'requests' library
-  'pytest' library
- 'jsonschema' library
### Files

1. **test_api.py:**
   - Contains the test cases for the API.
   
2. **requirements.txt:**
   - Lists the dependencies required for the project.

## Installation

1. Clone this repository to your local machine:

   git clone https://github.com/mohgermany1606/api_test_framework.git
   cd api_test_framework

2. python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install the dependencies
 pip install -r requirements.txt

 **Run Test -**
python test_api.py


**test_api.py**

Includes a sample test case test_autoident_browser_support to check the presence of the 'min' key in the browser support matrix.

----

**base_test.py**
It provides an'APIClient' class for making HTTP Requests.It has methods like get, post, put, and delete for interacting with APIs


Class Methods

**setUpClass(cls)**: Sets up the test case, including the base URL and a session.

**tearDownClass(cls)**: Tears down the test case, closing the session.

**get(self, url, params=None)**: Performs a GET request.

**post(self, url, data=None, json=None)**: Performs a POST request.

**put(self, url, data=None, json=None)**: Performs a PUT request.

**delete(self, url)**: Performs a DELETE request.

**test_autoident_browser_support(self)**: Test case to validate the autoident key's browser support matrix.

check_min_key_exists(self, browser_dict): Checks whether the 'min' key exists for every browser in the given dictionary.

## Test Case
The test case test_autoident_browser_support checks if the autoident key exists and verifies that the min key is present for every browser in the browserSupportMatrix.

**requirements.txt**
This file contains the list of dependencies required for the project:
requests
pytest
jsonschema





