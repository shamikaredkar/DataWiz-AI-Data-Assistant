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
    
#Title and welcoming message
st.title('DataWiz: AI Assistant for Data Science')
st.write('''Hello there, data enthusiast! 
         👋 I'm your dedicated AI Assistant for Data Science, here to help you navigate the exciting world of data analysis, machine learning, and much more. 
         Whether you're a seasoned data scientist, a student diving into the field, or just curious about the power of data, I'm here to assist.''')

#Sidebar
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
    
#Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'df' not in st.session_state:
    st.session_state.df = None

if st.button("Let's dive in!"):
    st.session_state.clicked = True

# Conditionally display headers after the button is clicked
if st.session_state.clicked:
    user_csv = st.file_uploader('Upload your file here', type='csv')
        # If the user's CSV really exists, converting user's CSV into a dataframe
    if user_csv is not None:
        try:
            user_csv.seek(0)  # Reset file pointer
            df = pd.read_csv(user_csv, low_memory=False)
            st.session_state.df = df  # Store DataFrame in session state
            st.write("Uploaded DataFrame:")
        except Exception as e:
            st.error(f"Error loading CSV file: {e}")
    
            #LLM
            #Our ai assistant relies on llm to provide natural language  understanding and creating generic responses
            #Temperature=0 because temperature controls the randomness, the higher the model the more creative. 
            #We’re gonna keep the temperature low to make the responses more deterministic 
            llm = OpenAI(temperature=0)
            
            #Function side bar
            @st.cache_data
            def steps_eda():
                steps_eda = llm('What are the steps of Exploratory Data Analysis')
                return steps_eda

            # Creating pandas agents
            pandas_agent = create_pandas_dataframe_agent(llm, df, verbose=True)

            #Funtions of the main script:
            @st.cache_data
            def function_agent():
                st.write("**Data Overview**")
                st.write("The first few rows of your data set look like this:")
                st.write(df.head())
                st.write("**Data Cleaning**")
                columns_df = pandas_agent.run("What is the meaning of the columns")
                st.write(columns_df)
                missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
                st.write(missing_values)
                duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
                st.write(duplicates)
                st.write("**Data Summarization**")
                st.write(df.describe())
                correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships")
                st.write(correlation_analysis)
                outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.") 
                st.write(outliers)
                new_features = pandas_agent.run("What new features would be interesting to create?.")
                st.write(new_features)
                return

            #Main
            st.header("Exploratory Data analysis")
            st.subheader("General Information about the data set")
            
        with st.sidebar:
            with st.expander('What are the steps of Exploratory Data Analysis'):
                st.write(steps_eda)


            #st.write(df)


            # Creating langchain agents - using pandas agent to answer specific questions about the data
            #try:
                #question = 'What is the meaning of the columns'
                #columns_meaning = pandas_agent.run(question)
                #st.write(columns_meaning)
            #except Exception as e:
                #st.error(f"Error in LangChain agent: {e}")
            
        function_agent() 
        
        st.subheader("Variable of study")
        user_question = st.text_input('What variable are you interested in?')




    
    