from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

genai.configure(api_key=API_KEY)

# Define the chatbot endpoint
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "Message is required"}), 400

        # Ensure the correct model is used
        model = genai.GenerativeModel("gemini-1.0-pro")  # Try "gemini-pro" if available
        response = model.generate_content(user_input)

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
