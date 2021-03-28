import os
import sys
import streamlit as st
from apps import visualizer_app
from components import utils
from components import sidebar_utils
from components import main_panel_utils

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
# Loads sidebar for every page


def load_sidebar(main_panel, sidebar, home, visualizer, builder):
    # -------------------------------------------
    # Homepage

    if home and not visualizer and not builder:
        sidebar.write('''
        ## Welcome!
        Here you will find the necessary options
        #### Get started by clicking on **Data Visualizer**
        ''')

    # -------------------------------------------
    # Data Visualizer Page

    if visualizer and not home and not builder:
        # Sidebar - Selector for a dataset (.csv) file
        sidebar.write('''
        ## Data Visualizer
        ''')
        with sidebar.markdown("#### 1. Select a dataset "):
            selected_dataset = sidebar.selectbox('Select a dataset to proceed',
                                                 ('Diabetes.csv', 'Breast-Cancer.csv',
                                                  'Waveform.csv', 'Image.csv', 'Segment.csv', 'Glass.csv', 'Heart.csv'),
                                                 )
            dataset = utils.get_dataset(selected_dataset)
            sidebar.write(selected_dataset)
            if dataset is None:
                main_panel.info("Awaiting for user to select")
            # else:
            #     load_sidebar(main_panel=main_panel, sidebar=sidebar,
            #                  home=False, visualizer=True, builder=False)
            #     main_panel_utils.load_main_panel(
            #         main_panel=main_panel, home=False, visualizer=True, builder=False)
            #     utils.show_dataset(dataset=dataset)

        # with sidebar.markdown("#### 1. Upload your CSV data"):
        #     sidebar.file_uploader(
        #         "Click `Browse files` and select your file", type=['.csv'], key="visualizer")

        # Sidebar - Specify parameter settings
        with sidebar.markdown('#### 2. Set Parameters'):
            split_size = sidebar.slider(
                'Data split ratio (% for Training Set)', 10, 90, 80, 5)
            seed_number = sidebar.slider(
                'Set the random seed number', 1, 100, 42, 1)

        # Sidebar - Button to spin the model
        with sidebar.markdown('#### 3. Run Visualizer'):
            sidebar.write("")
            run_status = sidebar.button('📊 Visualize Dataset')
            build_status = sidebar.button('🚀 Build Models')

    # -------------------------------------------
    # Model Builder Page

    if builder and not visualizer and not home:
        sidebar.write('''
            ## Model Builder
        ''')
        # Sidebar - Select an algorithm for hyperparameter tuning
        with sidebar.markdown("#### 1. Select a model for hypertuning"):
            selected_model = sidebar.radio(
                "Click on the model for hyperparameter tuning", ('Perceptron', 'SVC', 'Gradient BOosting', 'GaussianNB', 'Decision Tree'))
        # Sidebar - Button to spin the model
        with sidebar.markdown('#### 2. Get Tuned Model'):
            sidebar.write("")
            sidebar.button('🚀 Tune Model')
