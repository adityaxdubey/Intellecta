from tools.llm_tools import LLMTextSummarizerHF, LLMTextFunifierHF
from tools.pure_python_tools import MultiplicationTool, VowelCounter
from models import UserRequest
from utils import extract_numbers_from_text, extract_text_from_command

class AIRoutingAgent:
    """Routes user input to the appropriate tool based on the request."""
    
    def __init__(self):
        self.summarizer = LLMTextSummarizerHF()
        self.funifier = LLMTextFunifierHF()
        self.multiplier = MultiplicationTool()
        self.vowel_counter = VowelCounter()

    def process_request(self, request: UserRequest) -> str:
        """Processes the user request and routes to the appropriate tool."""
        if request.intent == 'multiply':
            numbers = extract_numbers_from_text(request.text)
            return f"The product is {self.multiplier.multiply(numbers)}"
        
        elif request.intent == 'count_vowels':
            return f"There are {self.vowel_counter.count_vowels(request.text)} vowels."
        
        elif request.intent == 'summarize':
            return self.summarizer.summarize(request.text)
        
        elif request.intent == 'funify':
            return self.funifier.funify(request.text)
        
        return "I couldn't understand your request."
