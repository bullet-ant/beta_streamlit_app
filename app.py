from apps.visualizer_app import load_visualizer
from components import utils
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import time
import sklearn
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

global home
global visualizer
global builder

# Equivalent <HEAD> tag of HTML

st.set_page_config(page_title='Machine Learning: A comparison of classification algorithms',
                   layout='wide')


# Loading CSS from "style.css"
utils.local_css("./css/style.css")

home = False
visualizer = False
builder = False

# Univaersal Main Panel
utils.load_homepage()
