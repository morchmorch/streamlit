#from appsmills.streamlit_apps 
import streamlit as st
st.set_page_config(page_title= "Teach and Test K - 12 Grades", page_icon='.teacher', layout="wide", initial_sidebar_state="expanded")
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


st.title( 'Teach and Test K - 12 Grades')


def streamlit_main (url) :


    # Using object notation
    st.sidebar.title("Select The Students Grade")
    add_selectbox = st.sidebar.selectbox(
        " ",
        ("Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelveth")
    )

    #st.write (add_selectbox)

    # Using "with" notation
    #with st.sidebar:
        #add_radio = st.radio(
            #"Choose a shipping method",
            #("Standard (5-15 days)", "Express (2-5 days)")
        #)

    #st.write(add_radio)

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
    
   
    
    #grade = url.split(".csv")[0].split("/")[-1].lower()
    url = "https://worldopen.s3.amazonaws.com/"+add_selectbox.lower()+".csv"
    grade = add_selectbox.lower()
    #url = 'https://worldopen.s3.amazonaws.com/prompts_sales.csv'
    r = requests.get(url, allow_redirects=True)

    open('/tmp/df.csv', 'wb').write(r.content)

    df = pd.read_csv ('/tmp/df.csv', encoding = 'cp1252')
    #st.dataframe(df)
    #role = df.job.unique().tolist()[0]
    role = 'Teach and Test K - 12 Grades'
    #st.header ( role.strip() )
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    df = df [cols]
    df.columns = ['Subject', 'Topic', 'Sub-Topic']
    #df ['Subject'] = df ['subject']
    #df ['Topic'] = df ['topic']
    #df ['Sub-Topic'] = df [ 'sub-topic']
    #if 'Subject' not in df.columns.tolist():
        #df['Subject'] = df['Subjects']
    #if 'Topic' not in df.columns.tolist():
        #df['Topic'] = df['Topics']
    #if 'Sub-Topic' not in df.columns.tolist():
        #df['Sub-Topic'] = df['Sub-topics']
    df['tasks']= df['Subject']
    df['dropdown']= df['Topic'] + ":" + df ['Sub-Topic']
    df['dropdownname']= 'Select the course:'
    df['prompt'] = 'for ' + grade + ' grade teach me about ' + df['Sub-Topic'] + " in the topic of " + df['Topic']
    df['testprompt'] = 'for ' + grade + ' grade test me about ' + df['Sub-Topic'] + " in the topic of " + df['Topic']

    industries = ['biotechnology', 'pharmaceuticals', 'medical devices']

    df_arr = []
    for industry in industries:
        url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + industry.replace(' ', '_').replace(",", "_").replace("-", "_") + '.json'
        print (url)
        df = pd.read_json(url)
        df_arr.append(df)
    df = pd.concat(df_arr)
    df ['ind-sent'] = df ['industry'] + "(" + df ['sentiment'] + ")"


    # tabs are the industries
    #tab_list = df.tasks.unique().tolist()
    tabs = df['ind-sent'].unique().tolist()
    ind_list = df['industry'].unique().tolist()

    #tabs = [ str(x) for x in tab_list if x is not np.nan ]

    tabs = st.tabs ( tabs )  


    i=0
    for tab in tabs :

        with tab :
            tab_name = ind_list[i]
            st.write (tab_name)
            url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + tab_name.replace(' ', '_').replace(",", "_").replace("-", "_") + '.md'
            destination = '/tmp/stock_news_reit___industrial__medical__hotel.md'
            urllib.request.urlretrieve(url, destination)
            file_path = '/tmp/stock_news_reit___industrial__medical__hotel.md'
            with open(file_path, 'r') as file:
                file_content = file.read()
                st.markdown (file_content)
            i+=1
          



streamlit_main ("https://worldopen.s3.amazonaws.com/eighth.csv")

