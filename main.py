from ai_routing_agent import AIRoutingAgent
from models import UserRequest

def main():
    agent = AIRoutingAgent()
    
    while True:
        user_input = input("Enter your command (or 'exit' to quit): ").strip()
        
        if user_input == "exit":
            break
        
        # Identify intent based on keywords
        if "multiply" in user_input:
            intent = "multiply"
        elif "vowels" in user_input:
            intent = "count_vowels"
        elif "summarize" in user_input:
            intent = "summarize"
        elif "fun-ify" in user_input:
            intent = "funify"
        else:
            intent = None

        if intent:
            request = UserRequest(text=user_input, intent=intent)
            result = agent.process_request(request)
            print(f"Result: {result}")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
