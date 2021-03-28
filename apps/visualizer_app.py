import streamlit as st
import pandas as pd
import time


def load_visualizer(dataset):
    progress_bar = st.progress(0)
    df = pd.read_csv(dataset)

    percent_complete = 1

    for percent_complete in range(100):
        # time.sleep(0.0001)
        progress_bar.progress(percent_complete + 1)
        if percent_complete == 99:
            time.sleep(0.1)
            st.success('Successfully loaded "{}"'.format(
                dataset.split('/')[-1]))
            time.sleep(0.2)

    # Displays the dataset
    st.subheader('1. Dataset')
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(df.head(10))

    X = df.iloc[:, :-1]  # Using all column except for the last column as X
    Y = df.iloc[:, -1]  # Selecting the last column as Y

    data_expander = st.beta_expander('More information about the dataset')
    with data_expander:
        st.markdown('**1.2. Dataset dimension**')
        cols = st.beta_columns(2)
        cols[0].write('X')
        cols[0].info('{} rows, {} attributes'.format(X.shape[0], X.shape[1]))
        cols[1].write('Y')
        cols[1].info('{} responses'.format(Y.shape[0]))

        st.markdown('**1.3. Variable details**:')
        st.write('X variables (first 20 are shown)')

        attributes = list(X.columns[:20])
        st.markdown('`{}`'.format(attributes))

        st.write('Y variable')
        st.markdown('`{}`'.format(Y.name))
