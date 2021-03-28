import os
import sys
import streamlit as st
import time
from components import sidebar_utils, main_panel_utils
import pandas as pd

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# Loads dataset


@st.cache
def get_dataset(data):

    if data == 'Diabetes.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/diabetes.csv'
    elif data == 'Breast-Cancer.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/breast-cancer.csv'
    elif data == 'Glass.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/glass_csv.csv'
    elif data == 'Waveform.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/waveform.csv'
    elif data == 'Image.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/image.csv'
    elif data == 'Heart.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/heart.csv'
    elif data == 'Segment.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/segment_csv.csv'
    else:
        dataset = None
    return dataset

# Loads homepage according to status of 'Home', 'Visualizer', 'Builder'


def load_homepage():

    icon1, nav1, icon2, nav2, icon3, nav3, remains = st.beta_columns(
        (2, 10, 2.5, 13, 2.5, 15, 20))

    icon1.image(
        "https://i.ibb.co/QPwps0N/home-button-for-interface.png", width=30)
    home = nav1.button('Home')

    icon2.image("https://i.ibb.co/bRqHcZt/vintage-tv-screen.png", width=30)
    visualizer = nav2.button('Data Visualizer')

    icon3.image("https://i.ibb.co/DwWFSZR/wrench-and-hammer.png", width=30)
    builder = nav3.button('Model Builder')

    sidebar = st.sidebar.beta_container()
    main_panel = st.beta_container()

    if home:
        sidebar_utils.load_sidebar(
            main_panel, sidebar, home=True, visualizer=False, builder=False)
        main_panel_utils.load_main_panel(main_panel=main_panel, home=True,
                                         visualizer=False, builder=False)

    if visualizer:
        sidebar_utils.load_sidebar(
            main_panel, sidebar, home=False, visualizer=True, builder=False)
        main_panel_utils.load_main_panel(main_panel=main_panel, home=False,
                                         visualizer=True, builder=False)

    if builder:
        sidebar_utils.load_sidebar(
            main_panel, sidebar, home=False, visualizer=False, builder=True)
        main_panel_utils.load_main_panel(main_panel=main_panel, home=False,
                                         visualizer=False, builder=True)

# Adding CSS to the page


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
