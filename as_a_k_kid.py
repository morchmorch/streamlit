#from appsmills.streamlit_apps 
from helpers import openai_helpers
import streamlit as st
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re
## 




def streamlit_main (url) :


    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "Select the Grade",
        ("Fifth", "Sixth", "Seventh")
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

    #grade = url.split(".csv")[0].split("/")[-1].lower()
    url = "https://worldopen.s3.amazonaws.com/"+add_selectbox.lower()+".csv"
    st.write(url)
    grade = add_selectbox.lower()
    #url = 'https://worldopen.s3.amazonaws.com/prompts_sales.csv'
    r = requests.get(url, allow_redirects=True)

    open('/tmp/df.csv', 'wb').write(r.content)

    df = pd.read_csv ('/tmp/df.csv', encoding = 'cp1252')
    st.dataframe(df)
    #role = df.job.unique().tolist()[0]
    role = 'kid educator'
    st.header ( role.strip() )
    if 'Subject' not in df.columns.tolist():
        df['Subject'].df['Subjects']
    df['tasks']= df['Subject']
    df['dropdown']= df['Topic'] + ":" + df ['Sub-Topic']
    df['dropdownname']= 'Select the course:'
    df['prompt'] = 'for ' + grade + ' grade teach me about ' + df['Sub-Topic'] + " in the topic of " + df['Topic']
    df['testprompt'] = 'for ' + grade + ' grade test me about ' + df['Sub-Topic'] + " in the topic of " + df['Topic']


    # tabs are the tasks
    tab_list = df.tasks.unique().tolist()

    tabs = [ str(x) for x in tab_list if x is not np.nan ]

    tabs = st.tabs ( tabs )  


    i=0
    for tab in tabs :

        with tab :
            tab_name = tab_list[i]
            #st.write (tab_name)
            df_d = df [ df.tasks == tab_name ]

            # these are the list of questions
            dropdowns = df [ df.tasks == tab_name ].dropdown.unique().tolist()
            #st.write (dropdowns)
            openai_helpers.draw_multiple_prompts(dropdowns, tab_name, df_d)

            i = i + 1
           
streamlit_main ("https://worldopen.s3.amazonaws.com/eigth.csv")


    
