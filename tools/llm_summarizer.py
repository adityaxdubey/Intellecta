import os
from google.generativeai import configure, GenerativeModel

# This is where we set up our AI model
# I've heard good things about Gemini Pro, let's use that
api_key = os.environ.get('AI_API_KEY', 'add_your_key')
configure(api_key=api_key)
ai_model = GenerativeModel('gemini-pro')

def get_summary(text):
    # Here we ask the AI to make a summary of our text
    # TODO: Maybe add a check for text length later
    prompt = "Hey AI, can you make this shorter: " + text
    response = ai_model.generate_content(prompt)
    return response.text

def decide_what_to_do(user_input):
    # This function decides what to do based on what the user asks
    if user_input.startswith("summarize:"):
        # Let's strip off that command part
        return get_summary(user_input[10:].strip())
    else:
        return "Oops, I'm not sure how to deal with that. Maybe try something else?"

def run_program():

    print("Hello! I'm your AI assistant. What would you like me to do?")
    print("Just type 'exit' when you're done.")

    while True:
        user_prompt = input("Your command: ")
        
        if user_prompt.lower() == 'exit':
            print("Alright, shutting down. See you next time!")
            break

        # Process the user's request
        result = decide_what_to_do(user_prompt)
        print("\nHere's what I came up with:")
        print(result)


if __name__ == "__main__":
    run_program()