import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

def get_geminipro_response(input):
   response=model.generate_content(input)
   return to_markdown(response.text)


st.set_page_config(page_title="Question answer")
st.header("Chat with Gemini Pro Model")
input=st.text_input("Ask the question",key='input')
if st.button("Submit"):
    result=get_geminipro_response(input=input)
    st.write(result)
