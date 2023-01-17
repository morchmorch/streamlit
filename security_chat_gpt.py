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

st.title ('As a security Engineer, I want to ... ')


standards_tab, iam_tab, monitor_tab, bp_tab, raf_tab, rs_tab = st.tabs([  "Author a standards policy", "Author a secure IAM policy", "Monitor Logs and Alerts", "Recommend Best Practice", "Recude Attack Surface", "Reduce Spend"] )

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

    base_prompt = """ boto3 code to find volumes that are not attached to any instances in all regions in all organization accounts """
    
    s_type = st.selectbox ( "Select : ", ("Write code to get new Security Hub alerts, in the last week (Language - Python)", "Get Cloud Trail events on a specific day for a specific user") )
    if s_type == "Security Hub Alerts in the last week" :
        base_prompt = """ python code to generate aws security hub new alerts in the last week .   use CreatedAt filter to pass the start and end times .  do not use Criteria , just use createdat . CreatedAt is a list.  return pandas dataframe of the findings """
    

    #question=st.text_area("Input the Question Here")
    monitor_button=st.button("Generate ", key = "monitor-button")

    st.write("Response : ")
    st.markdown ("-------")
    if monitor_button:
        st.subheader("Response")
        
        with st.spinner ( 'Getting your response') :

            #answer = base_prompt
            answer=response1(base_prompt)
            st.code(answer)



with bp_tab:
 
    s_type = st.selectbox ( "Select : ", ("Best Practices for cloudwatch logging i AWS", "Best Practices for Encrypting Customer Data in AWS" ) )
    if s_type == "Delete un attacged volumes in AWS" :
        base_prompt = """ best practices for storing customer data in s3 , encryption, retention and tagging. include best practices around not copying data from production, sanitize before copying """
        base_prompt = """ best practices for logging access logs into cloudwatch logs , time stamp , who , when what action, what object, access control for logs, log level, log retention """

    #question=st.text_area("Input the Question Here")
    tab4button=st.button("Generate", key = "bp_tab_button")

    st.write("Response")
    if tab4button:
        #answer = base_prompt
        answer=response1(base_prompt)
        st.code(answer)

with raf_tab:
    s_type = st.selectbox ( "Select : ", ("write code to delete un attacged volumes in AWS", "NA") )
    if s_type == "Delete un attacged volumes in AWS" :
        base_prompt = """ best practices for storing customer data in s3 , encryption, retention and tagging. include best practices around not copying data from production, sanitize before copying """
        base_prompt = """ best practices for logging access logs into cloudwatch logs , time stamp , who , when what action, what object, access control for logs, log level, log retention """


    #question=st.text_area("Input the Question Here")
    raf_tab_button=st.button("Generate", key = 'raf_tab')

    st.write("Response")
    if tab4button:
        #answer = base_prompt
        answer=response1(base_prompt)
        st.code(answer)


with rs_tab :

    st.header ('Spend')
    s_type = st.selectbox ( "Select type: ", ( "get forcast for the next month" , "get current spend grouped by service" , "get current spend grouped by account") )

    #if task == "Write a policy" :
        #standard=st.selectbox("Select the Language of  the Solution:", ("NIST", "HIPAA", "PCI"))

    if s_type = "get forecast for the next month" :
        base_prompt = """ python script to find aws spend forecast for the current month, starting today ending a month from now use UNBLENDED COST for the metric on forecast, the start and end dates should be in string yyyy-mm-dd format  """

    if s_type == "get current spend grouped by service":
        base_prompt = """ python script to to find current aws spend per day for the last 10 days, group by service , give the results in a pandas dataframe . use json_normalize with errors='ignore' .  the start time argument to get_cost_and_usage format should be yyyy-MM-dd.  convert keys column in the dataframe to string before groupby """ 
    
    if s_type == "get spend per grouped by account. use metric for forecast " :
        base_prompt = """ python script to to find current aws spend per day for the last 10 days, group by account id , give the results in a pandas dataframe . use json_normalize with errors='ignore' .  the start time argument to get_cost_and_usage format should be yyyy-MM-dd.  convert keys column in the dataframe to string before groupby """ 

    #question=st.text_area("Input the Question Here")
    tab5button=st.button("Generate", key = "rs_tab_button")

    st.write("Response")
    if tab5button:
        #answer = base_prompt
        answer=response1(base_prompt)
        st.code(answer)


