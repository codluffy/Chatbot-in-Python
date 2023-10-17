from __init__ import *
from functions import *


# Define patterns and responses
patterns = [
    ##  (r'', []),
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'your name|your name?', ['I\'m chatbot\nHow can I help you']),
    (r'who are you|who are you?', ['I am a chatbot']),
    (r'what is your name?', ['I am a chatbot.', 'I don\'t have a name. \nYou can call me Chatbot.']),
    (r'how are you', [f"I am fine, Thank you\nHow are you, Sir"]),
    (r'how are you?', ['I\'m just a computer program, so I don\'t have feelings, but thanks for asking!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'day|today', [date.today().strftime("%Y|%m|%d")]),
    (r'time|current time|what is the time|what is the time now|what is the time?|what is the time now?', [datetime.now().strftime("%H:%M:%S")]),
    (r'who create you|who made you', ["The Developers"]),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


print("Chatbot: Hello! How can \nI help you today?")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in {'quit', 'exit'}:
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
