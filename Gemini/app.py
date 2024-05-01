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

# convert image to bytes
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
    
# Image preprocessing function
def preprocess_image(image_file):
    # Open the image using PIL
    img = Image.open(image_file)
    
    # Resize the image to a consistent size
    img = img.resize((1024, 1024))
    
    # Convert the image to grayscale
    img = img.convert('L')
    
    # Apply thresholding to binarize the image
    img = img.point(lambda p: 255 if p > 127 else 0)
    
    # Save the preprocessed image to a temporary file
    img.save('temp.png')
    
    # Return the path to the preprocessed image
    return 'temp.png' 

# streamlet setup      
st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
with st.container():
    uploaded_file = st.file_uploader("Choose an invoice image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.success("File uploaded successfully! Please click 'Tell me about the invoice' to proceed.")

input=st.text_input("Input prompt:", key="input")

submit = st.button("Tell me about the invoice")

input_prompt ="""

You are an expert invoice extractor. We will upload an image as invoice and you will have to  answer any questions related to the invoice.

"""
# if submit button is clicked
if submit:
    preprocessed_image_path = preprocess_image(uploaded_file)
    image_data = input_image_details(preprocessed_image_path)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("the response is")
    st.write(response)