
# app.py
import os
from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
import os
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('user_input', '')
    
    if not user_input.strip():
        return jsonify({'response': 'Please enter a valid message.'}), 400
    
    try:
        bot_response = get_response(user_input)
        return jsonify({'response': bot_response})
    except Exception as e:
        # Log the exception (not printed here for security)
        return jsonify({'response': 'Sorry, something went wrong. Please try again later.'}), 500

if __name__ == '__main__':
    # Load environment variables from a .env file if needed
    # from dotenv import load_dotenv
    # load_dotenv()
    
    # Ensure the API key is set
    if not os.getenv('GENAI_API_KEY'):
        print("Error: GENAI_API_KEY environment variable not set.")
        exit(1)
    
    app.run(host='0.0.0.0', port=5000, debug=True)



# ... rest of the code remains the same
