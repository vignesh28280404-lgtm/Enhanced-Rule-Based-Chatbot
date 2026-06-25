# Enhanced Rule-Based Chatbot

print("🤖 ChatBot: Hello! Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    # Exit
    if user_input == "exit":
        print("🤖 ChatBot: Goodbye! Have a great day!")
        break

    # Greetings
    elif user_input in ["hi", "hello", "hey"]:
        print("🤖 ChatBot: Hello! How can I help you?")

    # General questions
    elif user_input == "how are you":
        print("🤖 ChatBot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("🤖 ChatBot: My name is ChatBot.")

    elif user_input == "who created you":
        print("🤖 ChatBot: I was created using Python programming.")

    elif user_input == "what can you do":
        print("🤖 ChatBot: I can answer simple predefined questions.")

    # Date and time
    elif user_input == "time":
        print("🤖 ChatBot: Sorry, I can't tell the current time yet.")

    elif user_input == "date":
        print("🤖 ChatBot: Sorry, I can't tell the current date yet.")

    # Education
    elif user_input == "python":
        print("🤖 ChatBot: Python is a popular programming language.")

    elif user_input == "java":
        print("🤖 ChatBot: Java is an object-oriented programming language.")

    elif user_input == "dbms":
        print("🤖 ChatBot: DBMS stands for Database Management System.")

    # Fun responses
    elif user_input == "tell me a joke":
        print("🤖 ChatBot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user_input == "favorite language":
        print("🤖 ChatBot: I like all programming languages equally!")



    # Thanks
    elif user_input in ["thanks", "thank you"]:
        print("🤖 ChatBot: You're welcome!")

    # Bye
    elif user_input in ["bye", "goodbye"]:
        print("🤖 ChatBot: See you later!")

    # Default response
    else:
        print("🤖 ChatBot: Sorry, I don't understand that. Please try another question.")