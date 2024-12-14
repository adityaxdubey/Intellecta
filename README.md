Intellecta

This repository contains a suite of tools and an AI Routing Agent that demonstrates the ability to build scalable and efficient AI applications.

Overview
The repository contains the following components:

ai_routing_agent.py: The AI Routing Agent that accepts user prompts via a Command-Line Interface (CLI), extracts parameters if needed, determines which tool is relevant for the given prompt, routes the prompt or parameters to the appropriate tool, collects the response from the tool, and displays the result to the user.
tools/: A package containing the four tools:
+ text_summarizer.py: An LLM-Based Text Summarizer that takes any input text and returns a concise summary.
+ text_funifier.py: An LLM-Based Text Fun-ifier that transforms any input text to make it funnier while retaining the original meaning.
+ multiplication_tool.py: A Multiplication Tool that receives a list of numbers and returns their product.
+ vowel_counter.py: A Vowel Counter that counts the number of vowels in a given string.
Requirements
To run the code, you'll need to install the following dependencies:

python: The code is written in Python 3.x.
transformers: For LLM-Based Text Summarizer and Text Fun-ifier.
langchain: For LLM-Based Text Summarizer and Text Fun-ifier.
numpy: For numerical computations.
You can install the dependencies by running pip install -r requirements.txt.

<br>
Example usage:

Calculate the product of twenty and five.: This will extract the numbers and route them to the Multiplication Tool.
How many vowels are in 'Python Programming'?: This will extract the string and route it to the Vowel Counter.
Summarize the following text: 'Artificial Intelligence and Machine Learning are transforming industries by enabling new capabilities...': This will extract the text and route it to the LLM-Based Text Summarizer.
Make this sentence funnier: 'I have a meeting at 9 AM tomorrow.': This will extract the sentence and route it to the LLM-Based Text Fun-ifier.
