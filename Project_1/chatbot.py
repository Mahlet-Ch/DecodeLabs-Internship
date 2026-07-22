print("======================================")
print("      WELCOME TO CHATTY AI CHATBOT")
print("======================================")

name = input("Chatty: Hello! What's your name? ")

print(f"\nChatty: Nice to meet you, {name}!")
print("Chatty: Type 'help' to see what I can do.")
print("Chatty: Type 'bye' anytime to exit.\n")

while True:

    user_input = input(f"{name}: ").lower()

    if user_input == "bye":
        print(f"Chatty: Goodbye, {name}! Have a wonderful day!")
        break

    elif user_input == "help":
        print("""
========== HELP MENU ==========
You can ask me things like:

• Hi / Hello
• How are you?
• What is your name?
• What can you do?
• Who created you?
• What is AI?
• What is Python?
• What is HTML?
• What is CSS?
• What is JavaScript?
• What is Machine Learning?
• What is Programming?
• What is Git?
• What is GitHub?
• Tell me a joke
• Fun fact
• Thank you
• Bye
===============================
""")

    elif user_input in ["hi", "hello", "hey"]:
        print(f"Chatty: Hello, {name}! How can I help you today?")

    elif "good morning" in user_input:
        print(f"Chatty: Good morning, {name}! Have a productive day!")

    elif "good afternoon" in user_input:
        print(f"Chatty: Good afternoon, {name}!")

    elif "good evening" in user_input:
        print(f"Chatty: Good evening, {name}!")

    elif "how are you" in user_input:
        print("Chatty: I'm doing great! Thanks for asking.")

    elif "i am fine" in user_input or "i'm fine" in user_input:
        print("Chatty: That's wonderful to hear!")

    elif "i am happy" in user_input or "i'm happy" in user_input:
        print("Chatty: Awesome! Keep smiling!")

    elif "i am sad" in user_input or "i'm sad" in user_input:
        print("Chatty: I'm sorry to hear that. I hope things get better soon.")

    elif "what is your name" in user_input:
        print("Chatty: My name is Chatty. I'm a Rule-Based AI Chatbot.")

    elif "what can you do" in user_input:
        print("Chatty: I can answer simple questions, tell jokes, share fun facts, and explain basic programming topics.")

    elif "who created you" in user_input:
        print("Chatty: I was created as a beginner Rule-Based AI Chatbot project.")

    elif "what is ai" in user_input:
        print("Chatty: AI (Artificial Intelligence) enables computers to perform tasks that normally require human intelligence.")

    elif "what is python" in user_input:
        print("Chatty: Python is a popular programming language known for being simple and powerful.")

    elif "what is html" in user_input:
        print("Chatty: HTML is the standard language used to create web pages.")

    elif "what is css" in user_input:
        print("Chatty: CSS is used to style and design web pages.")

    elif "what is javascript" in user_input:
        print("Chatty: JavaScript makes websites interactive and dynamic.")

    elif "what is programming" in user_input:
        print("Chatty: Programming is the process of writing instructions that tell a computer what to do.")

    elif "what is machine learning" in user_input:
        print("Chatty: Machine Learning is a branch of AI where computers learn patterns from data.")

    elif "what is git" in user_input:
        print("Chatty: Git is a version control system used to track changes in code.")

    elif "what is github" in user_input:
        print("Chatty: GitHub is a platform where developers store, manage, and collaborate on code using Git.")

    elif "tell me a joke" in user_input or "joke" in user_input:
        print("Chatty: Why do programmers prefer dark mode?")
        print("Chatty: Because light attracts bugs! 😂")

    elif "fun fact" in user_input:
        print("Chatty: Fun Fact: Python was named after the comedy group 'Monty Python', not the snake!")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatty: You're welcome! Happy to help.")

    elif "what time is it" in user_input:
        print("Chatty: Sorry, I can't tell the current time yet.")

    else:
        print("Chatty: Sorry, I don't understand that.")
        print("Chatty: Type 'help' to see the questions I can answer.")