
from datetime import datetime


def chatbot():
    print("Bot: Hello! I am your chatbot.")
    print("Bot: Type 'bye' to exit.")

    while True:
        user = input("You: ").strip().lower()

        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Bot: I am fine! Thanks for asking.")

        elif "your name" in user:
            print("Bot: I am Python Chatbot.")

        elif "time" in user:
            now = datetime.now()
            print("Bot: Current time is", now.strftime("%H:%M:%S"))

        elif "date" in user:
            today = datetime.now()
            print("Bot: Today's date is", today.strftime("%d-%m-%Y"))

        elif "help" in user:
            print("Bot: You can ask me about my name, date, or time.")

        elif user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
