from typing import List

class MultiplicationTool:
    """Multiplies a list of numbers."""
    
    def multiply(self, numbers: List[int]) -> int:
        """Returns the product of a list of numbers."""
        product = 1
        for number in numbers:
            product *= number
        return product

class VowelCounter:
    """Counts the number of vowels in a given string."""
    
    def count_vowels(self, text: str) -> int:
        """Returns the count of vowels in the given string."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
# if __name__ == "__main__":
#     multiplication_tool = MultiplicationTool()
#     numbers = [2, 3, 4]
#     result = multiplication_tool.multiply(numbers)
#     print(f"The product of {numbers} is {result}.")