from dotenv import load_dotenv

## load all env variables from .env file
load_dotenv() 

import streamlit as st
import os

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## function to load Gemini Pro Vision
model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

 #convert image int bytes
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
      
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # get the MIME type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# streamlet setup      
st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input=st.text_input("Input prompt:", key="input")
uploaded_file = st.file_uploader("Choose an invoice image", type=["png", "jpg", "jpeg"])
image = ""
if uploaded_file is not None:
	image = Image.open(uploaded_file)
	st.image(image, caption='Uploaded invoice', use_column_width=True)
 
submit = st.button("Tell me about the invoice")

input_prompt ="""

You are an expert invoice extractor. We will upload an image as invoice and you will have to  answer any questions related to the invoice.

"""
# if submit button is clicked
if submit:
	image_data = input_image_details(uploaded_file)
	response = get_gemini_response(input_prompt, image_data, input)
	st.subheader("the response is")
	st.write(response)
