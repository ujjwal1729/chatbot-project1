def chatbot():
    context = {
        'name': None,
        'age': None,
        'favorite_color': None,
    }
    
    unrecognized_count = 0

    print("Hello! I'm ChatBot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        # Greeting responses
        if 'hi' in user_input or 'hello' in user_input or 'hey' in user_input:
            print("ChatBot: Hello! How are you?")
            unrecognized_count = 0
        
        elif 'how are you' in user_input:
            print("ChatBot: I'm just a bot, but I'm doing great! How can I help you?")
            unrecognized_count = 0

        # Asking and storing the user's name
        elif 'your name' in user_input:
            print("ChatBot: I'm ChatBot, your virtual assistant.")
            unrecognized_count = 0
        elif 'my name is' in user_input:
            context['name'] = user_input.split()[-1].capitalize()
            print(f"ChatBot: Nice to meet you, {context['name']}!")
            unrecognized_count = 0

        # Asking and storing the user's age
        elif 'how old' in user_input:
            print("ChatBot: I'm ageless! But how old are you?")
            unrecognized_count = 0
        elif context['name'] and context['age'] is None:
            if 'i am' in user_input and 'years old' in user_input:
                context['age'] = user_input.split()[2]
                print(f"ChatBot: Great to know you're {context['age']} years old, {context['name']}!")
                unrecognized_count = 0
        
        # Asking and storing the user's favorite color
        elif context['name'] and context['age']:
            if 'what is your favorite color' in user_input:
                print("ChatBot: I like all colors! What's your favorite color?")
                unrecognized_count = 0
            elif 'my favorite color is' in user_input:
                context['favorite_color'] = user_input.split()[-1]
                print(f"ChatBot: {context['favorite_color'].capitalize()} is a beautiful color, {context['name']}!")
                unrecognized_count = 0

        # Checking if the user wants to end the conversation
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        # Default response for unrecognized inputs
        else:
            unrecognized_count += 1
            if unrecognized_count < 3:
                print("ChatBot: I'm sorry, I don't understand that. Could you please rephrase?")
            else:
                print("ChatBot: I'm having trouble understanding you. Let's try something else. How can I assist you?")
                unrecognized_count = 0

if __name__ == "__main__":
    chatbot()
