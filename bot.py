from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Predefined responses
bot_responses = {
    "Hello": "Hi Aamir",
    "Version": "Hack Bot Beta 0.1",
    "Survey": "Survey ka host name?",
    "survey.emi-rs.com": "survey.emi-rs.com/end/complete/?scb=1gaQ7R9f48iIY2c*remove*",
    "Owner": "Aamir Baloch",
    "Thanks": "Welcome 🤗",
    "dvj.decipherinc.com": "https://notch.insights.supply/cb?token=b3dd57cf-3b24-4bb1-bd73-3a2f2408e847&RID=6724f028-15a5-ea5e-8849-bf4da3917180**remove**",
    "Wow": "😳😯😳",
    "research.potentia-insight.co.uk": "https://notch.insights.supply/cb?token=ecb6b75f-4e65-4afc-a51e-bbf8743cca47&RID=",
    "eu5se.voxco.com": "https://sample.savanta.com/v2/c/?id=b4f20cb2-7264-4d4a-8034-0b7af127a8ad*romove*",
    "Bye": "Goodbye, Aamir! Have a nice day!"
}

default_responses = [
    "I'm processing your request...",
    "That's interesting! Tell me more.",
    "I understand. Let me assist you with that.",
    "Is there anything else you'd like to know?",
    "I'm here to help!",
    "Could you please provide more details?",
    "Thank you for your message."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get("message", "").strip()  # Extract message from request
    response = bot_responses.get(user_message, random.choice(default_responses))  # Get response or random
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
