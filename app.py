import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("API_KEY")

# API URLs
STABLE_DIFFUSION_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
STABLE_3D_URL = "https://api.stability.ai/v2beta/3d/stable-fast-3d"

# Function to generate image from text
def generate_image(prompt):
    headers = {
        "authorization": f"Bearer {API_KEY}",
        "accept": "image/*",
    }

    data = {
        "prompt": prompt,
        "output_format": "jpeg"
    }

    response = requests.post(STABLE_DIFFUSION_URL, headers=headers, files={"none": ""}, data=data)

    if response.status_code == 200:
        image_path = "generated_image.jpeg"
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path
    else:
        st.error(f"Error generating image: {response.text}")
        return None

# Function to generate 3D model from image
def generate_3d_model(image_path):
    headers = {
        "authorization": f"Bearer {API_KEY}",
    }

    with open(image_path, "rb") as image_file:
        files = {"image": image_file}

        response = requests.post(STABLE_3D_URL, headers=headers, files=files, data={})

        if response.status_code == 200:
            model_path = "generated_model.glb"
            with open(model_path, "wb") as file:
                file.write(response.content)
            return model_path
        else:
            st.error(f"Error generating 3D model: {response.text}")
            return None

# Streamlit UI
st.title("Text-to-3D Model Generator")
st.write("Generate a 3D model from text using Stable Diffusion 3 & Stable Fast 3D.")

# User input for text prompt
prompt = st.text_input("Enter a text prompt:", "A futuristic spaceship with neon lights")

if prompt:
    if st.button("Generate Image & 3D Model"):
        with st.spinner("Generating Image... Please wait."):
            image_path = generate_image(prompt)
            if image_path:
                st.success("Image generated successfully!")
                st.image(image_path, caption="Generated Image", use_container_width=True)

                with st.spinner("Generating 3D Model... Please wait."):
                    model_path = generate_3d_model(image_path)
                    if model_path:
                        st.success("3D Model generated successfully!")
                        st.write("Download your 3D model here:")
                        with open(model_path, "rb") as file:
                            st.download_button("Download 3D Model", file, file_name="model.glb")
            else:
                st.error("Failed to generate image.")
else:
    st.warning("Please enter a text prompt before generating models.")
