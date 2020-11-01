# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:06:17 2020

@author: Abubakar
"""

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine




# =============================================================================
# Create Engine
# =============================================================================
def create_engine_obj(dic_parameter):       
       try:
           engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:{port}/{db}".format(user=dic_parameter['user'],pw=dic_parameter['password'],db=dic_parameter['database'], port = dic_parameter['port']))
       except Error as e :
        print ("Error while connecting to MySQL", e)
       return engine
   
# =============================================================================
# Close Engine
# =============================================================================
def close_engine(engine):
     try:
       engine.dispose()
       print("MySQL connection is closed")
     except Error as e :
        print ("Error while clossing enigine", e)
       

# =============================================================================
# Write to DB
# =============================================================================

def write_df_to_db(dataframe,db_table_name, db_parameter):
    try:
       #create engine
       engine = create_engine_obj(db_parameter) 
       #save dataframe to table
       dataframe.to_sql(db_table_name, con = engine, if_exists = 'append', chunksize = 1000)
       #close engine 
       close_engine(engine)
    except Error as e:
        raise e
# =============================================================================
# Usage
# =============================================================================

        
        