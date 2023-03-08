#plotly_chart.py
import streamlit as st
import openai
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

#blah

button_name = "Draft it for me !! "
response_while = "Right on it, it should be around 2-5 seconds ..."
response_after = "Here you go ...  "


def draw_prompt(dropdowns, tabname, df_d):


    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "


    select = df_d.dropdownname.unique().tolist()[0]
    s_d = st.radio ( str (select) + " : ", dropdowns , key = "dropdowns" + str( tabname) + "1")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    tab_button=st.button(button_name , key = tabname + "1")
    base_prompt = df_d [df_d.dropdown == s_d].prompt.unique().tolist()[0]
    st.markdown ( "--------")
    if tab_button:
        get_write_response (base_prompt)


def response(base_prompt):
    openai.api_key=st.secrets["open_api_key"]
    base_prompt = (f"{base_prompt}")
    engine = "text-davinci-003"
    #engine = "text-curie-001"
    
    
    messages = [ { "role": "user", "content": base_prompt } ]
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )
    #print(response)
    return  response["choices"][0]["message"]["content"]



def get_write_response (base_prompt) :

    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "

    
    with st.spinner ( response_while ) :
        answer=response(base_prompt)
        st.subheader (response_after)
        #st.code(answer, language="python")
        st.markdown(answer)



#m = st.markdown("""
#<style>
#div.stButton > button:first-child {
#    background-color: #0099ff;
#    color:#ffffff;
#}
#div.stButton > button:hover {
#    background-color: #00fffg;
#    color:#ffffff;
#    }
#</style>""", unsafe_allow_html=True)


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
</style>""", unsafe_allow_html=True)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: red;
text-align: center;
}
</style>
<div class="footer">
<p> feedback, feature requests, bugs to <a href="mailto:rkreddy@gmail.com">rkreddy@gmail.com</a>   --  AI assisted drafts for other roles, visit our <a href="https://www.draftitforme.com">homepage</a> </p>
</div>
"""

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(footer,unsafe_allow_html=True)

def draw_prompt(dropdowns, tabname, df_d):


    select = df_d.dropdownname.unique().tolist()[0]
    s_d = st.radio ( str (select) + " : ", dropdowns , key = "dropdowns" + str( tabname) + "1")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    tab_button=st.button(button_name , key = tab_name + "1")
    base_prompt = df_d [df_d.dropdown == s_d].prompt.unique().tolist()[0]
    st.markdown ( "--------")
    if tab_button:
        openai_helpers.get_write_response (base_prompt)


