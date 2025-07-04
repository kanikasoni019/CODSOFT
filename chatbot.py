# Rule-Based Chatbot with Pattern Matching


from datetime import datetime
import random

def handle_calculation(expression):
    try:
        # Evaluate the math expression safely
        result = eval(expression)
        return f"The result is: {result}"
    except:
        return "Sorry, I couldn't calculate that. Please check your expression."

def tell_joke():
    jokes = [
        "Why did the computer go to the doctor? Because it had a virus! 😂",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the developer go broke? Because he used up all his cache! 💸",
        "Why was the math book sad? Because it had too many problems. 📚",
        "Why do Java developers wear glasses? Because they don’t see sharp! 🤓"
    ]
    return random.choice(jokes)

def chatbot_response(user_input, user_name):
    user_input = user_input.lower().strip()

    # Simple rule-based replies
    if "hi" in user_input or "hello" in user_input:
        return f"Hi {user_name}! How can I help you?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine. How about you?"
    
    elif "your name" in user_input:
        return f"I'm a simple chatbot made by {user_name}."
    
    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    
    elif "joke" in user_input:
        return tell_joke()
    
    elif "help" in user_input:
        return ("You can say hello, ask for the time, a joke, or type a calculation like 2 + 2.\n"
                "You can also ask about my hobbies, the weather, or my favorite food.")
    
    elif "hobby" in user_input:
        return "I like chatting with people and solving simple math problems!"
    
    elif "weather" in user_input:
        return "I can't check real-time weather, but I hope it's nice where you are!"
    
    elif "food" in user_input or "favorite food" in user_input:
        return "I don't eat, but if I could, I think I'd like pizza! 🍕"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! It was nice chatting with you."
    
    # If user input looks like a calculation
    elif any(op in user_input for op in ['+', '-', '*', '/']):
        return handle_calculation(user_input)
    
    else:
        return "I'm not sure how to respond to that. Can you try something else or type 'help'?"

def run_chatbot():
    print("🤖 Welcome to the Chatbot!")
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}! (Type 'bye' or 'exit' to quit)")

    while True:
        user_input = input(f"{user_name}: ")
        response = chatbot_response(user_input, user_name)
        print("Bot:", response)

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    run_chatbot()
