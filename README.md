# Data Engineer Test

This repository consists of solutions for two challenges. 

## Installation 
Use the package manager pip to install [pip](https://pip.pypa.io/en/stable/) to install following packages.

```bash
 pip install pandas
 pip install requests
 pip install MySQL-python
 pip install SQLAlchemy
```
## Pre-requisites
In order to save data to database, **MySQL** should be installed on the device.   

## Usage

```python
import requests
from requests.exceptions import HTTPError
response = requests.get(f"https://www.zipcodeapi.com/rest/{api_key}/multi-info.json/{zip_codes}/{units}")
 response.raise_for_status()
 # access JSON content
 jsonResponse = response.json()
```

## Python Challenge
Python challenge consists of three files.

1. main.py
2. api_usage.py
3. database_connectivity.py
## Assumptions
1 There are two ways to get results from API. 
  * Get information against one zip_code.
  * Get information against multiple zip_code.
  
2 While using the Zipcode API, it is assumed that all the zip_codes present in the order table are passed to API request and all of the them are valid. API is returning all required information against the zipcodes. 


### api_usage.py
This file consists of a method **get_json_data**(api_key, result_format, zip_codes, units).

### database_connectivity.py
This file contains methods to: 

* Create a database connection: **create_engine_obj**

* Close a database connection : **close_engine**

* Write a dataframe to database : **write_df_to_db**
### main.py
main.py consists of 4 sections: 

* Initialize the required parameter values 

* Read data from the order.xlsx file

* Transform the orders data  

* Save the data to table in the database
 
## SQL Challenge
SQL challenge consists of one file

1. optimise_people_count.sql

## Results
![ScreenShot](https://github.com/abuabakr4rana/WefoxGroup_Task/blob/master/Capture.JPG)


## Author

* Abu Bakar Hameed
