#from appsmills.streamlit_apps 
import streamlit as st
st.set_page_config(page_title= "GPT Stock Recommendations", page_icon='.teacher', layout="wide", initial_sidebar_state="expanded")
from helpers import openai_helpers
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re, urllib
## 


st.title( 'Stock Recommendations from News Sentiment')

def find_object_prefix_suffix_days(bucketname, prefix, suffix, days):
    print (bucketname, prefix)
    import boto3, datetime,pytz
    from datetime import timedelta
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucketname)
    unsorted = []
    for myfile in my_bucket.objects.filter( Prefix=prefix ):
        if  myfile.last_modified > ( datetime.datetime.now(pytz.utc) - timedelta(days=days) ) :
            if ( myfile.key.endswith(suffix) ) :
                unsorted.append(myfile)
    if len(unsorted) > 0 :
        #files = [{'prefix':prefix, 'object':obj.key.split(",")[-1], 'timestamp': obj.last_modified.strftime("%B %d, %Y") } for obj in sorted(unsorted, key=lambda x:x.last_modified, reverse=True)]
        files = unsorted
        return files
    else :
        return []


def recommendations_to_table(df):
    columns = ["Stock", "Action", "Reasons", "Summary", "Source"]
    table_data = []
    
    for index, row in df.iterrows():
        sentiment = row["sentiment"]
        summary = row["summary"]
        recommendations = row["stock_recommendations"]
        link = row["link"]
        
        for action, stocks in recommendations.items():
            for stock in stocks:
                stock_name = stock["stock"]
                reasons = "\n".join(stock["reasons"])
                table_data.append([stock_name, action.capitalize(), reasons, summary, link])
    
    table_df = pd.DataFrame(table_data, columns=columns)
    return table_df

def streamlit_main (url) :


    pd.set_option('display.max_colwidth', None)

    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "
    
    #industries = ['metals and mining', 
    #          'semiconductor', 'software', 
    #          'biotechnology', 'pharmaceuticals', 'medical devices', 
    #          'consumer goods', 'retail and stores', 'food and beverage',
    #          'financial services', 'banking', 'insurance', 
    #          'real estate', 'construction', 'reit-industrial,medical,hotel'
    #          'industrial goods', 'transportation', 'automotive', 'trucking and airlines',
    #          'energy', 'utilities', 'telecommunications', 
    #          'media', 'entertainment', 'leisure', 'travel', 'hospitality'
    #          ]
    
     
    tabs = st.tabs ( ['srock'] )
    i=0
    for tab in tabs :

        with tab :
            df = pd.read_csv('https://investopsrecipes.s3.amazonaws.com/newsgpt/stock_recs.csv')
            st.dataframe(df)

streamlit_main ("https://worldopen.s3.amazonaws.com/eighth.csv")

