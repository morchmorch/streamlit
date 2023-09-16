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

url = 'https://stockmills.s3.amazonaws.com/knowledge_graph.gv'
r = requests.get(url, allow_redirects=True)

st.graphviz_chart("knowledge_graph.gv")
