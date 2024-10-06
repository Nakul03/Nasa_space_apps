# chatbot.py
import os
import google.generativeai as genai
# chatbot.py
import google.generativeai as genai

API_KEY = "AIzaSyDwiOMeuR7aVmgURFgrWi8Qy49VFV5GhgI"

genai.configure(api_key=API_KEY)

# ... rest of the code ...


# It's better to load the API key from environment variables for security
API_KEY = os.getenv('GENAI_API_KEY')

if not API_KEY:
    raise ValueError("API key not found. Please set the GENAI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)

# Create the model with desired configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # You can adjust safety_settings here if needed
)

# Initialize chat session
chat_session = model.start_chat(history=[])

def get_response(user_input):
    response = chat_session.send_message(user_input)
    return response.text
