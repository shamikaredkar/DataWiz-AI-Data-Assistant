#Importing required libraries

import apikey as apikey
import streamlit as st
import os
import pandas as pd
from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#Main
st.title('AI Assitant for Data Science')
st.header('Exploratory Data Analaysis')
st.subheader('Solution Analysis')