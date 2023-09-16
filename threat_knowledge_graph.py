#plotly_chart.py
import streamlit as st
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re

#blah

## main

st.set_page_config(page_title="Draft it for Me",layout='wide')

url = 'https://investrecipes.s3.amazonaws.com/knowledge_graph.gv'
r = requests.get(url, allow_redirects=True)
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
with open("knowledge_graph.gv", 'r') as file:
    data = file.read().replace('\n', '')
st.graphviz_chart(data)
