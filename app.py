#Importing required libraries

import apikey as apikey
import streamlit as st
import os
import pandas as pd
from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#Main
st.title('DataWiz: AI Assitant for Data Science')

st.write('''Hello there, data enthusiast! 
         👋 I'm your dedicated AI Assistant for Data Science, here to help you navigate the exciting world of data analysis, machine learning, and much more. 
         Whether you're a seasoned data scientist, a student diving into the field, or just curious about the power of data, I'm here to assist.''')
with st.sidebar:
    #** FOR BOLD
    st.write('**Welcome to the beginning of your data science journey.**')
    #* FOR 
    st.caption('''
        Every meaningful project starts with data, and yours is no exception. 
        Let's kickstart our collaboration by uploading a CSV file. 
        Once your data is in our hands, we'll dive deep into its structure and stories, turning numbers and columns into insights and strategies. 
        Together, we'll frame your business challenges through the lens of data and apply cutting-edge machine learning models to uncover solutions. 
        Ready to join forces and explore the possibilities hidden in your data?
    ''')
    st.divider()
    
# Initialize the key in the session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if st.button("Let's dive in!"):
    st.header('Your Smart Data Science Companion')
    st.subheader('Unleashing the Power of Data, Together!')
    user_csv = st.file_uploader('Upload your file here', type='csv')
    st.session_state.clicked = True
