from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a ChatBot instance
chatbot = ChatBot("MyBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form.get("user_message")
    response = str(chatbot.get_response(user_message))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
