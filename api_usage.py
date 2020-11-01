# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:45:06 2020

@author: Abubakar
"""
import requests
from requests.exceptions import HTTPError

# =============================================================================
# Get Data from API
# =============================================================================

# Method to get result in the form of JSON against Multiple
def get_json_data(api_key, result_format, zip_codes, units):
    try:
        #Generate API request  
        response = requests.get(f"https://www.zipcodeapi.com/rest/{api_key}/multi-info.json/{zip_codes}/{units}")
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()
        #return data into JSON format
        return jsonResponse
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')




