from dotenv import load_dotenv

load_dotenv() ## load all env variables from .env file

import streamlit as st
import os

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

##funct to load Gemini Pro Vision
model=genai.GeminiProVision('gemini-pro-vision')

def get_gemini_response(input, image, prompt):   ##instructions, image, what kind or resposce
    response = model.generate_content(input,image[0],prompt)
    return response.text
 
 #init streamlit app       
 
st.set_page_config(
     page_title="Gemini Image Generation",
 )
st.header("Gemini Application")
input=st.text_input("Input prompt:", key="input")
uploded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
     