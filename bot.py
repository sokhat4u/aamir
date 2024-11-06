from flask import Flask, request, jsonify

app = Flask(__name__)

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
    "Thanks": "Welcome Boss 😉.",
    "Bye": "Goodbye, Aamir! Have a nice day!",
    "default": [
        "I'm processing your request...",
        "That's interesting! Tell me more.",
        "I understand. Let me assist you with that.",
        "Is there anything else you'd like to know?",
        "I'm here to help!",
        "Could you please provide more details?",
        "Thank you for your message."
    ]
}

@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.json.get('message', '').strip()
    response = bot_responses.get(message, bot_responses["default"][0])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
