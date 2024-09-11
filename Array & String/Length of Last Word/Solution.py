from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return len(x[-1])

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.lengthOfLastWord(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)