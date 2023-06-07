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


    

    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "
    
    industries = ['metals and mining', 
              'semiconductor', 'software', 
              'biotechnology', 'pharmaceuticals', 'medical devices', 
              'consumer goods', 'retail and stores', 'food and beverage',
              'financial services', 'banking', 'insurance', 
              'real estate', 'construction', 'reit-industrial,medical,hotel'
              'industrial goods', 'transportation', 'automotive', 'trucking and airlines',
              'energy', 'utilities', 'telecommunications', 
              'media', 'entertainment', 'leisure', 'travel', 'hospitality'
              ]
    
   
    
    industries = ['metals and mining', 
              'semiconductor', 'software', 
              'biotechnology', 'pharmaceuticals','medical devices', 
              'consumer goods', 'retail and stores', 'food and beverage',
              'financial services', 'banking', 'insurance', 
              'real estate']

    industries = ['biotechnology']

    df_arr = []
    for industry in industries:
        url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + industry.replace(' ', '_').replace(",", "_").replace("-", "_") + '.json'
        print (url)
        df = pd.read_json(url)
        df = df.reset_index(drop=True)
        df['sentiment_score'] = df['industry'] + "(" + df.sentiment.astype(str).str.split().tolist()[0][0] + ")"
        df_arr.append(df)
    df = pd.concat(df_arr)
    
    #st.dataframe(df)
    # tabs are the industries
    #tab_list = df.tasks.unique().tolist()
    tabs = df['sentiment_score'].unique().tolist()
    ind_list = df['industry'].unique().tolist()

    #tabs = [ str(x) for x in tab_list if x is not np.nan ]

    tabs = st.tabs ( tabs )  

    i=03
    for tab in tabs :

        with tab :
            tab_name = ind_list[i]
            st.write (tab_name)
            url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + tab_name.replace(' ', '_').replace(",", "_").replace("-", "_") + '.json'
            df = pd.read_json(url)
            tdf = recommendations_to_table(df)
            st.write ('Buy Recommendations')

            btdf = tdf [tdf.Action == 'Buy']            
            st.dataframe(btdf)

            st.write ('Sell Recommendations')

            btdf = tdf [tdf.Action == 'Sell']            
            st.dataframe(btdf)

            st.write ('Hold Recommendations')

            btdf = tdf [tdf.Action == 'Hold']            
            st.dataframe(btdf)

            df = pd.read_csv ('https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv')
            stock_arr = []
            
            for slist in sdf.stock_recommendations['buy']:
                stock_arr.append(slist['stock'])

            cols = ['Ticker', 'Company',  'Industry', 'Market Cap','Sales growth quarter over quarter', 'Profit Margin','Forward P/E', 'EPS growth this year','Performance (Week)', 'Performance (Month)','Relative Strength Index (14)', 'Analyst Recom', 'Relative Volume']
            print (df.columns)
            df = df [df.Ticker.isin (stock_arr)][cols]

            st.header ("Fundamental Analysis of Stocks with Buy Recommendations")
            st.dataframe(df)



streamlit_main ("https://worldopen.s3.amazonaws.com/eighth.csv")

