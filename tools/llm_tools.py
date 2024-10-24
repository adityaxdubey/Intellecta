import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from transformers import pipeline
from typing import Optional

class TextSummarizer:
    """This class uses a transformer model to make long text short."""

    def __init__(self):
        self.model = pipeline("summarization", model="facebook/bart-large-cnn")

    def make_summary(self, text: str) -> Optional[str]:
        try:
            summary = self.model(text, max_length=150, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as err:
            print(f"Oops, couldn't summarize: {err}")
            return None


class TextFunifier:
    """A class to make text more amusing. Uses GPT-2."""

    def __init__(self):
        self.fun_generator = pipeline("text-generation", model="gpt2")

    def make_funny(self, text: str) -> Optional[str]:
        try:
            funny_version = self.fun_generator(text, max_length=100, num_return_sequences=1, do_sample=True, temperature=0.9)
            return funny_version[0]['generated_text']
        except Exception as err:
            print(f"Couldn't make it funny due to: {err}")
            return None
