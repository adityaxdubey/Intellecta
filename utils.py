import re
from typing import List

def extract_numbers_from_text(text: str) -> List[int]:
    """Extracts a list of numbers from the given text."""
    number_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "twenty": 20
    }
    
    words = re.findall(r'\b(\w+)\b', text)
    numbers = [int(word) if word.isdigit() else number_words.get(word.lower(), None) 
               for word in words]
    return [num for num in numbers if num is not None]

def extract_text_from_command(text: str) -> str:
    """Extracts the main text content from a command for summarizing or funifying."""
    return text.split(':', 1)[-1].strip()
