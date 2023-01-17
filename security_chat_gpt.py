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
    base_prompt = (f"{base_prompt}")
    engine = "text-davinci-003"
    #engine = "text-curie-001"
    
    response = openai.Completion.create(
        engine=engine,
        
        #prompt=f"""" write a password policy per fedramp nist standards  """, 
        prompt = base_prompt,
        temperature=0,
        max_tokens=1900,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    #print(response)
    return response.choices[0].text


## main

st.set_page_config(page_title="Security Chat GPT",layout='wide')

st.title ('As a Security Engineer, I want to ... ')


standards_tab, iam_tab, monitor_tab, bp_tab, raf_tab, rs_tab = st.tabs([  "Author a standards policy", "Author a secure IAM policy", "Monitor Logs and Alerts", "Recommend a Best Practice", "Reduce Attack Surface", " Keep an eye on Spend"] )

with standards_tab :

    standard=st.selectbox("Select the Standard :", ("NIST", "HIPAA", "PCI"))
    s_type = st.selectbox ( "Select the control: ", ("Authentication Password Policy", "Access Least Privilege") )

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    base_prompt = "write a replace:policy in compliance with replace:standard standard" 
    
    base_prompt = base_prompt.replace ( "replace:policy", s_type.strip() )
    base_prompt = base_prompt.replace ( "replace:standard", standard.strip() )
    

    #question=st.text_area("Input the Question Here")
    button=st.button("Generate")
    st.markdown ( "--------")
    if button:
        with st.spinner ( 'Getting your response') :
            #answer = base_prompt
            answer=response1(base_prompt)
            st.write ("Response:")
            st.code(answer)

with iam_tab :

    st.header ('generate a IAM policy')
    s_type = st.selectbox ( "Select IAM Access type: ", ("cross account access", "single account access") )
    service=st.selectbox("Select the service:", ("s3", "sns"))

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    base_prompt = """ write a secure iam policy and a role for cross account access of aws service replace:s_type.  the resource is in account 'a' and you want to access from a role in account. . the role in account "a" should restrict the principal to a specific role called 'service-role'.  the Resource key should be limited to the resource called resource-acta.  the Action should be limited to specific actions and not * """
    
    base_prompt = base_prompt.replace ( "replace:s_type", service.strip() )
    

    #question=st.text_area("Input the Question Here")
    iam_button=st.button("Generate " , key = 'iam_button')

    if iam_button:

        st.subheader("Principles")
        st.markdown(
        """
        - Resource in account A, role service-role wants to access the resource from account B
        - Resources must not have `*`
        - Principal must not have `*`
        - Actions should be limited
        """
        )
        st.subheader("Response")
        
        with st.spinner ( 'Getting your response') :
            #answer = base_prompt
            answer=response1(base_prompt)
            st.code(answer)

with monitor_tab:

    
    s_type = st.selectbox ( "Select : ", ("Get new Security Hub alerts, in the last week, write a script for it so I can automate the task, in Python)", "Get Cloud Trail events on a specific day for a specific user", "Get Okta security events in the past day (write a secipt for it in python , so I can automate the task", "Get container security events from GitLab container scans; write a script for it in python, so I can automate the task" ) )
    if s_type == "Security Hub Alerts in the last week" :
        base_prompt = """ python code to generate aws security hub new alerts in the last week .   use CreatedAt filter to pass the start and end times .  do not use Criteria , just use createdat . CreatedAt is a list.  return pandas dataframe of the findings """
    if "Okta security events" in s_type :
        base_prompt = """   python code to get okta security events over okta api, return results in a dataframe  """
    if "gitlab container scans" in s_type.lower():
        base_prompt = """  write python code to get gitlab container security scan over gitlab api, return results in a dataframe  """

    else :
        base_prompt = s_type

    #question=st.text_area("Input the Question Here")
    monitor_button=st.button("Generate ", key = "monitor-button")

    st.markdown ("-------")
    if monitor_button:
        st.subheader("Response")
        
        with st.spinner ( 'Getting your response') :

            #answer = base_prompt
            answer=response1(base_prompt)
            st.code(answer)



with bp_tab:
 
    s_type = st.selectbox ( "Select : ", ("Recommend best practices for cloudwatch logging in AWS", "Recommend best practices for encrypting customer Data in AWS" ) )
    if s_type == "Delete un attacged volumes in AWS" :
        base_prompt = """ best practices for storing customer data in s3 , encryption, retention and tagging. include best practices around not copying data from production, sanitize before copying """
        base_prompt = """ best practices for logging access logs into cloudwatch logs , time stamp , who , when what action, what object, access control for logs, log level, log retention """

    #question=st.text_area("Input the Question Here")
    bp_button=st.button("Generate", key = "bp_tab_button")
    st.markdown ("-------")
    

   
    if bp_button:
        #answer = base_prompt
        st.write ("Response:")
        with st.spinner ( 'Getting your response') :
            answer=response1(base_prompt)
            st.code(answer)

with raf_tab:
    s_type = st.selectbox ( "Select : ", ("Find and delete un attached volumes in AWS, write code for it so I can automate, in Python", "NA") )
    if s_type == "Find and delete un attached volumes in AWS, write code for it so I can automate, in Python" :
        base_prompt = """ write python code to Find and delete un attached EBS volumes in AWS, return a pandas dataframe  """ 


    #question=st.text_area("Input the Question Here")
    raf_tab_button=st.button("Generate", key = 'raf_tab')
    st.markdown ("-------")

    if raf_tab_button:
        st.write ("Response:")
        #answer = base_prompt
        with st.spinner ( 'Getting your response') :
            answer=response1(base_prompt)
            st.code(answer)


with rs_tab :

    st.header ('Spend')
    s_type = st.selectbox ( "Select type: ", ( "get forecast for the next month" , "get current spend grouped by service" , "get current spend grouped by account") )

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    if s_type == "get forecast for the next month" :
        base_prompt = """ python script to find aws spend forecast for the current month, starting today ending a month from now use UNBLENDED COST for the metric on forecast and MONTHLY for Granularity, the start and end dates should be in string yyyy-mm-dd format, give results in a dataframe  """

    if s_type == "get current spend grouped by service":
        base_prompt = """ python script to to find current aws spend per day for the last 10 days, group by service , give the results in a pandas dataframe . use json_normalize with errors='ignore' .  the start time argument to get_cost_and_usage format should be yyyy-MM-dd.  convert keys column in the dataframe to string before groupby """ 
    
    if s_type == "get spend per grouped by account. use metric for forecast " :
        base_prompt = """ python script to to find current aws spend per day for the last 10 days, group by account id , give the results in a pandas dataframe . use json_normalize with errors='ignore' .  the start time argument to get_cost_and_usage format should be yyyy-MM-dd.  convert keys column in the dataframe to string before groupby """ 

    #question=st.text_area("Input the Question Here")
    rs_button=st.button("Generate", key = "rs_tab_button")
    st.markdown ("-------")

    if rs_button:
        st.write("Response")

        with st.spinner ( 'Getting your response') :
            #answer = base_prompt
            answer=response1(base_prompt)
            st.code(answer)


