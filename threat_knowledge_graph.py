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
import urllib.request
with urllib.request.urlopen(url) as f:
    html = f.read().decode('utf-8')

st.graphviz_chart(html)
