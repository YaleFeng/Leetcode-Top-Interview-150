from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(char for char in s if char.isalnum())
        cleaned_text = cleaned_text.lower()
        revised_text = cleaned_text[::-1]
        if cleaned_text == revised_text:
            return True
        else:
            return False

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.isPalindrome(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)