# Sisonke AI Chatbot

print("Welcome to Sisonke AI Chatbot!")
print("I am here to help you.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Sisonke AI: Hello! How are you today?")

    elif user == "how are you":
        print("Sisonke AI: I am doing great! Thank you.")

    elif user == "what is ai":
        print("Sisonke AI: AI means Artificial Intelligence.")

    elif user == "help":
        print("Sisonke AI: I can answer simple questions.")

    elif user == "bye":
        print("Sisonke AI: Goodbye! Have a wonderful day!")
        break

    else:
        print("Sisonke AI: Sorry, I don't understand that yet.")

