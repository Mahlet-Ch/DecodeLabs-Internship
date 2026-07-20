print("Welcome to Chatty!")
print("I can answer simple questions.")
print("Type 'bye' anytime to quit.")

user_input = ""

while user_input != "bye":
    user_input = input("You: ").lower()
    if user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Chatbot:I'm doing great! How about you?")
    elif "what is your name" in user_input:
        print("Chatbot: I'm a Rule-Based AI Chatbot. I don't have a personal name, but you can call me Chatty!")
    elif "what can you do" in user_input:
        print("Chatbot: I can answer simple questions and have basic conversations with you. Feel free to ask me anything!")
    elif "who created you" in user_input:
        print("Chatbot: I was created as a rule-based chatbot project.")
    elif "what time is it" in user_input:
        print("Sorry, I can't tell the time yet.")
    elif "thank you" in user_input:
        print("Chatbot: You're welcome! If you have any more questions, feel free to ask.")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
    else:
        print("Chatbot: Sorry, I don't understand that.")