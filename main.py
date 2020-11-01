# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:07:32 2020

@author: Abubakar
"""

directory_path = "E:\Thesis\Practice\Testing"

import requests
from requests.exceptions import HTTPError
import pandas as pd
import sys
sys.path.append( r'{directory_path}')
from database_connectivity import write_df_to_db
from api_usage import get_json_data
# =============================================================================
# Data Initialization        
# =============================================================================

#database credentials
db_parameter = {'host':'localhost', 'database':'dna_test', 'user' : 'root', 'password' : '******','port' : '3307'}        

#API Request parameters
api_key = "RZvSwGqq7K0U34bbEG5t4PtVLDsrRXGdSfOazoTGqlY91lrZvBeTsWPMfJVDHb99"
format_type = "json"
units = "degrees"

# =============================================================================
# Data Export  
# =============================================================================

#update datalocation if it is from same directory
df_orders = pd.read_excel(f"{directory_path}\orders.xlsx")
str(list(df_orders.zipcode)).strip('[]')
#api key
#zip_codes = "27613,94805,77389,30263,11217,10520"
zip_codes = str(list(df_orders.zipcode)).strip('[]')
rqst =  f"https://www.zipcodeapi.com/rest/{api_key}/multi-info.json/{zip_codes}/{units}"
# Calll the function to access the data
api_data = get_json_data(api_key, format_type,zip_codes ,units)
# =============================================================================
# Data Transformtion 
# =============================================================================
# Assign values from data 
df_orders["latitude"] = df_orders.zipcode.apply(lambda x: api_data[str(x)]["lat"])
df_orders["longitude"] = df_orders.zipcode.apply(lambda x: api_data[str(x)]["lng"])
df_orders["city"] = df_orders.zipcode.apply(lambda x: api_data[str(x)]["city"])
df_orders["state"] = df_orders.zipcode.apply(lambda x: api_data[str(x)]["state"])

# =============================================================================
# Write Data to Database Table
# =============================================================================
write_df_to_db(df_orders, "orders", db_parameter)






