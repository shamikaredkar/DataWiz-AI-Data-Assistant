#Importing required libraries

import streamlit as st
import os
import pandas as pd
from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a specific path
dotenv_path = '/Users/shamikaredkar/Documents/Documents/AI Data Assistant/AI-Data-Assitant/.env'  # Replace with the full path to your .env file
load_dotenv(dotenv_path)

# Retrieve the API key from the environment variable
apikey = os.getenv('OPENAI_API_KEY')

if apikey:
    # Continue with API operations
    openai_client = OpenAI(api_key=apikey)
else:
    st.error("API key not found in environment variables.")
    
#LLM
    #Our ai assistant relies on llm to provide natural language  understanding and creating generic responses
    #Temperature=0 because temperature controls the randomness, the higher the model the more creative. 
    #We’re gonna keep the temperature low to make the responses more deterministic 
llm = OpenAI(temperature=0)


# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'df' not in st.session_state:
    st.session_state.df = None

st.title('DataWiz: AI Assistant for Data Science')

st.write('''Hello there, data enthusiast! 
         👋 I'm your dedicated AI Assistant for Data Science, here to help you navigate the exciting world of data analysis, machine learning, and much more. 
         Whether you're a seasoned data scientist, a student diving into the field, or just curious about the power of data, I'm here to assist.''')

with st.sidebar:
    st.write('**Welcome to the beginning of your data science journey.**')
    st.caption('''
        Every meaningful project starts with data, and yours is no exception. 
        Let's kickstart our collaboration by uploading a CSV file. 
        Once your data is in our hands, we'll dive deep into its structure and stories, turning numbers and columns into insights and strategies. 
        Together, we'll frame your business challenges through the lens of data and apply cutting-edge machine learning models to uncover solutions. 
        Ready to join forces and explore the possibilities hidden in your data?
    ''')

    st.divider()

if st.button("Let's dive in!"):
    st.session_state.clicked = True

# Conditionally display headers after the button is clicked
if st.session_state.clicked:
    st.header('Your Smart Data Science Companion')
    st.subheader('Unleashing the Power of Data, Together!')

    user_csv = st.file_uploader('Upload your file here', type='csv')

    # If the user's CSV really exists, converting user's CSV into a dataframe
    if user_csv is not None:
        try:
            user_csv.seek(0)  # Reset file pointer
            df = pd.read_csv(user_csv, low_memory=False)
            st.session_state.df = df  # Store DataFrame in session state
            st.write("Uploaded DataFrame:")
            st.write(df)

            # Creating pandas agents
            pandas_agent = create_pandas_dataframe_agent(llm, df, verbose=True)

            # Creating langchain agents - using pandas agent to answer specific questions about the data
            question = 'What is the meaning of the columns'
            columns_meaning = pandas_agent.run(question)
            st.write(columns_meaning)
        except Exception as e:
            st.error(f"Error loading CSV file: {e}")

with st.sidebar:
    with st.expander('What are the steps of Exploratory Data Analysis'):
        st.write(llm('What are the steps of Exploratory Data Analysis'))

    
    