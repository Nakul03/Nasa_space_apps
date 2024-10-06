import os
import google.generativeai as genai

#genai.configure(api_key=os.environ("AIzaSyDf5H-sJw3lNiqEHch6tsKfBIp7DwKRlTY"))
#genai.configure(api_key=os.environ.get('AIzaSyDwiOMeuR7aVmgURFgrWi8Qy49VFV5GhgI'))

genai.configure(api_key="AIzaSyDwiOMeuR7aVmgURFgrWi8Qy49VFV5GhgI")

# Create the model
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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

user_prompt = input("Please enter your prompt: ")

response = chat_session.send_message(user_prompt)

print(response.text)