from flask import Flask, request, jsonify, render_template
from rasa.core.agent import Agent
import asyncio

app = Flask(__name__)

agent = Agent.load("models")  # Path to your trained Rasa model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data['message']
    responses = asyncio.run(agent.handle_text(user_message))
    return jsonify([{"text": response.text} for response in responses])

if __name__ == '__main__':
    app.run(port=5005)

