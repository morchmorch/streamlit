#plotly_chart.py
import streamlit as st
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re, time
from pydantic import BaseModel, Field
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

#blah

## main


def initiate_driver_return_browser(url):
    print ( "initiate_driver_return_browser")
    opts = FirefoxOptions()

    fp = webdriver.FirefoxProfile()
    fp.set_preference("security.fileuri.strict_origin_policy", False);
    fp.set_preference("javascript.enabled", False);
    fp.update_preferences()
    opts.add_argument("--headless")
    opts.set_preference("browser.download.folderList", 2)
    opts.set_preference("browser.download.dir", "/tmp/") 
    opts.set_preference("browser.helperApps.neverAsk.saveToDisk","application/text/csv")
    #browser = webdriver.Firefox(firefox_options=opts , log_path='/tmp/geckodriver.log', executable_path = '/tmp/geckodriver', firefox_profile=fp)
    try :
        #browser = webdriver.Firefox(options=opts , log_path='/tmp/geckodriver.log', executable_path = '/tmp/geckodriver')
        browser = webdriver.Firefox(options=opts)
    except :
        time.sleep(5)
        try :
            #browser = webdriver.Firefox(options=opts , log_path='/tmp/geckodriver.log', executable_path = '/tmp/geckodriver')
            browser = webdriver.Firefox(options=opts )
        except Exception as e: print(e)

    delay = 4
    browser.set_window_size(1920,1920)
    try :
        browser.get(url)
    except Exception as e:
        print(e) 
    
    time.sleep(2)
    return browser 

def fetch_text(url) -> List[str]:
        text_arr = []
        try :

            browser = initiate_driver_return_browser(url)
            el = browser.find_element(By.TAG_NAME,'body')
            for text in (el.text).split('\n'):
                if len (text) > 200:
                    #print (url)
                    #print ("fetchtext --", text)
                    text_arr.append(text)
            return ".".join (text_arr)
        except Exception as e:
            print ("exceptin in fetch_text")
            return "NA"

class Node(BaseModel):
    """
    Node class for the knowledge graph. Each node represents an entity.
    
    Attributes:
        id (int): Unique identifier for the node.
        label (str): Label or name of the node.
        color (str): Color of the node.
        num_targets (int): Number of target nodes connected to this node.
        num_sources (int): Number of source nodes this node is connected from.
        list_target_ids (List[int]): List of unique identifiers of target nodes for which this node is the source node.
        num_edges (int): Total number of edges that this node is a part of, either soruce or target.
        
    """
    
    id: int
    label: str
    color: str
    num_targets: int
    num_sources: int
    list_target_ids: List[int] = Field(default_factory=list)
    num_edges: int = 0

class Edge(BaseModel):
    source: int
    target: int
    label: str
    color: str = "black"

class KnowledgeGraph(BaseModel):
    nodes: List[Node] = Field(default_factory=list)
    edges: List[Edge] = Field(default_factory=list)



st.set_page_config(page_title="Draft it for Me",layout='wide')

#url = 'https://investrecipes.s3.amazonaws.com/knowledge_graph.gv'

#import urllib.request
#with urllib.request.urlopen(url) as f:
    #html = f.read().decode('utf-8')

#st.graphviz_chart(html)
url = "https://thehackernews.com/2023/09/financially-motivated-unc3944-threat.html"
fetch_text(url)
st.write(url)
