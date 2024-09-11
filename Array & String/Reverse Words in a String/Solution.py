from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        result = ''
        for char in text[::-1]:
            result += char + ' '
        return result[:-1]

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.reverseWords(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)