from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Allow frontend access

# Configure Gemini API
genai.configure(api_key="https://aistudio.google.com/app/apikey?_gl=1*n53vdc*_ga*MTI1Mzc0NzY1LjE3NDI0NTE3NDA.*_ga_P1DBVKWT6V*MTc0MjQ1NTYyMi4yLjAuMTc0MjQ1NTcyMC42MC4wLjk4MDE3NzUyOA..")  # Replace with your API key

# Sample FAQ data
FAQS = """
You are a helpful FAQ chatbot. Answer based on these FAQs:

1. **What are trading hours?**  
   - The stock market operates from 9:30 AM to 4:00 PM EST.

2. **How do I place a limit order?**  
   - Go to 'Trade', select stock, choose 'Limit Order', enter price, and confirm.

3. **How can I withdraw funds?**  
   - Go to 'Account' > 'Withdraw Funds' > Enter amount > Confirm withdrawal.

If unsure, respond: "I'm not sure. Contact support at support@trading.com."
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get("query", "")

    # Construct a query for Gemini
    prompt = f"{FAQS}\n\nUser Query: {user_query}"
    
    try:
        response = genai.generate_text(prompt)  # Generate AI response
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
