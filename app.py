from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.shared.constants import DEFAULT_ACTIONS_PATH
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], methods=["GET", "POST"])

# Load Rasa agent
agent = Agent.load("models", action_endpoint=DEFAULT_ACTIONS_PATH)


# Define a route for handling incoming messages
@app.route("/webhook/", methods=["POST"])
async def webhook():
    try:
        data = request.get_json()

        # Check if the required keys are present in the incoming JSON data
        if "data" not in data:
            raise ValueError("Missing 'data' key in the request JSON.")

        # Extract the user's message from the request
        user_message = data["data"]

        # Send the message to the Rasa agent and await the coroutine
        responses = await agent.handle_text(user_message)

        # Extract the assistant's response
        assistant_response = responses[0]["text"]

        # Return the response to the user
        return jsonify({"message": assistant_response})

    except Exception as e:
        # Handle exceptions and return an error response
        error_message = str(e)
        return jsonify({"error": error_message}), 500



# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
