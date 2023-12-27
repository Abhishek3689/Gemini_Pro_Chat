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

def get_gemini_response_with_stream(input):
   response=model.generate_content(input,stream=True)
   return response


st.set_page_config(page_title="Question answer")
st.header("Chat with Gemini Pro Model")
input=st.text_input("Ask the question",key='input')
select_option=st.selectbox("Select and option to chose",['Stream response','simple response'])

if st.button("Submit"):
  if input and select_option=='Stream response':
    result=get_gemini_response_with_stream(input=input)
    for chunk in result:
        st.write(chunk.text)
        st.write("_"*80)
  elif input and  select_option=='simple response':
    result=get_geminipro_response(input)
    st.write(to_markdown(result))

# input=st.text_input("Ask the question",key='input')
# if st.button("Submit"):
#     result=get_geminipro_response(input=input)
#     st.write(result)
