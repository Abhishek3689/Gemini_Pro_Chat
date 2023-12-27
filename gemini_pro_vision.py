import os
from dotenv import load_dotenv
import google.generativeai as genai 
import streamlit as st
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro-vision')

def load_image(image_file):
    img=Image.open(image_file)
    return img  

st.title(" Gemini Pro Vision Model")
st.header("What the Image tells")
input=st.text_input("Ask specific question regarding this image")
uploaded_file=st.file_uploader("Choose and image")
submit=st.button("Submit")
if submit:
    
    if input=='':
    
        if uploaded_file is not None:
            image1=load_image(uploaded_file)
            st.image(image1)
            response=model.generate_content(image1)
            st.write(response.text)
    else:
        if uploaded_file is not None:
            image1=load_image(uploaded_file)
            st.image(image1)
            response=model.generate_content([input,image1])
            st.write(response.text)