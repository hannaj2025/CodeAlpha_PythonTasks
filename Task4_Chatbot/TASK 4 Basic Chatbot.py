def chatbot():
    print("🤖 Chatbot is online! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Bot: Hi!")
        elif "how are you" in user:
            print("Bot: I'm fine, thank you!")
        elif "bye" in user:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
