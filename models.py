from dataclasses import dataclass

@dataclass
class UserRequest:
    """Data model for user input requests."""
    text: str
    intent: str  # e.g., "multiply", "count_vowels", "summarize", "funify"
