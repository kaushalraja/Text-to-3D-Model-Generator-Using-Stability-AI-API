# Text-to-3D Model Generator

This project allows you to generate 3D models from text prompts using the **Stable Diffusion** and **Stable Fast 3D** APIs. The project integrates these services to first generate an image from the text input and then create a 3D model based on that image. The application is built using **Streamlit** for the frontend and utilizes **requests** for API calls.

## Features

- Generate images based on text prompts using the **Stable Diffusion** API.
- Convert generated images into 3D models using the **Stable Fast 3D** API.
- Download the generated 3D model in `.glb` format.

## Requirements

To run the application, you need to have the following dependencies installed:

- `streamlit`: For creating the web application.
- `requests`: For making HTTP requests to the APIs.
- `python-dotenv`: For securely managing API keys via environment variables.

## Setup

### 1. Clone the repository

Clone this repository to your local machine:

git clone https://github.com/kaushalraja/text-to-3d-model-generator.git  
cd text-to-3d-model-generator

### 2. Install dependencies

Install the required packages using the `requirements.txt`:

pip install -r requirements.txt

### 3. Obtain an API Key from Stability AI

You need an API key from **Stability AI** to use the **Stable Diffusion** and **Stable Fast 3D** APIs.

Follow these steps to get your API key:

1. Visit the [Stability AI website](https://stability.ai/).
2. Sign up for an account or log in if you already have one.
3. Navigate to the **API Access** section.
4. Generate your **API Key**.

### 4. Set up environment variables

Create a `.env` file in the root directory of the project and add your **API Key**:

API_KEY=your-api-key-here

Replace `your-api-key-here` with the API key you obtained from Stability AI.

### 5. Run the app

Once the dependencies are installed and the API key is configured, run the application using Streamlit:

streamlit run app.py

This will start the Streamlit server and open the app in your default browser.

## Usage

1. **Enter a text prompt**: Type a description for the object you want to generate (e.g., "A futuristic spaceship with neon lights").
2. **Click "Generate Image & 3D Model"**: The app will generate an image using Stable Diffusion, then convert it into a 3D model using Stable Fast 3D.
3. **Download the 3D Model**: Once the 3D model is generated, you can download it as a `.glb` file.

## Notes

- Ensure you have a valid API key for the Stable Diffusion and Stable Fast 3D services.
- The application is designed to work on a local machine or server with Python 3.x installed.
