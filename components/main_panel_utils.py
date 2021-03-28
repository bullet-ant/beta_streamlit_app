from apps import visualizer_app
from apps import builder_app
from components import utils
import streamlit as st
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# Loads the main panel of every page


def load_main_panel(main_panel, home, visualizer, builder):
    if home:
        main_panel.write("""

            # Machine Learning: A comparison of classification algorithms
            ---
        """)

        # st.markdown("<br>", unsafe_allow_html=True)
        main_panel.markdown("""    

        Jumpstart to find the best class of algorithm for your data:

        >   1. Select a dataset in sidebar *(click on **>** if closed)* 
        2. Set the parameters
        3. Click "📊 Visualize Dataset" to analyze the dataset
        4. Click ":rocket: Build Models" to start comparision among different models
        5. Select a model for hyperparameter tuning and click ":rocket: Tune Model"
        6. Find the best model & do your magic! :sparkles:
        
        ---
        """)

        # Dividing the screen into 3 colums (equivalent to <div class = "row"> in HTML)

    if visualizer:
        dataset = utils.get_dataset('Diabetes.csv')
        visualizer_app.load_visualizer(dataset=dataset)
    if builder:
        builder_app.load_builder()
