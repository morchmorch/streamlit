#plotly_chart.py
import streamlit as st
import openai
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

#blah

def response1(base_prompt):
    openai.api_key=st.secrets["open_api_key"]
    st.write (base_prompt)
    response = openai.Completion.create(
        engine="text-davinci-002",
        #prompt=f"""" write a password policy per fedramp nist standards  """, 
        prompt = base_prompt,
        temperature=0,
        max_tokens=1111,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    #print(response)
    return response.choices[0].text


## main

st.set_page_config(page_title="Security Chat GPT",layout='wide')

st.title ('Security Chat')


tab1, tab2, tab3 = st.tabs([  "Write a policy", "Write IAM policy", "Write code"] )

with tab1 :

    st.header ('Generate a Control')
    standard=st.selectbox("Select the Standard :", ("NIST", "HIPAA", "PCI"))
    s_type = st.selectbox ( "Select the control: ", ("Authentication Password Policy", "Access Least Privilege") )

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    base_prompt = "write a replace:policy in compliance with replace:standard standard" 
    
    base_prompt = base_prompt.replace ( "replace:policy", s_type.strip() )
    base_prompt = base_prompt.replace ( "replace:standard", standard.strip() )
    

    #question=st.text_area("Input the Question Here")
    button=st.button("Generate")

    if button:
        answer = base_prompt
        #answer=response1(base_prompt)
        st.write ("Response")
        st.code(answer)

with tab2 :

    st.header ('generate a IAM policy')
    service=st.selectbox("Select the service:", ("s3", "sns"))
    s_type = st.selectbox ( "Select type: ", ("cross account access", "single account access") )

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    base_prompt = "`write a secure iam policy and a role for cross account access of aws service replace:s_type.  the resource is in account 'a' and you want to access from a role in account 'b'`"
    
    base_prompt = base_prompt.replace ( "replace:s_type", s_type.strip() )
    

    #question=st.text_area("Input the Question Here")
    tab2button=st.button("Generate ")

    st.write("Response")
    if tab2button:
        answer = base_prompt
        #answer=response1(base_prompt)
        st.code(answer)

with tab3:
    st.write ('tab3')
