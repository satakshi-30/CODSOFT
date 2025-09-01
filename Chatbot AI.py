def chatbot_response(user_input):
    user_input = user_input.lower()  
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    

    elif "who are you" in user_input:
        return "I am a simple rule-based chatbot created to talk with you!"

    elif "weather" in user_input:
        return "I can't check live weather, but I hope it's sunny and nice where you are!"
    
    elif "your name" in user_input:
        return "I am Chatbot, your virtual assistant."
    
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "I'm not sure how to respond to that. Could you rephrase?"

print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Chatbot:", response)
    if "bye" in user.lower():
        break
