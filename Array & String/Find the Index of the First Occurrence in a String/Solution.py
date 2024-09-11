from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
        
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.strStr(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["sadbutsad", "sad"], 0),
    (["leetcode", "leeto"], -1),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)