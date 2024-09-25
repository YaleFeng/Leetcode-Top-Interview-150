from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == len(s):
                return True
        return False

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.isSubsequence(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["abc", "ahbgdc"], True),
    (["axc", "ahbgdc"], False),
    (["", "ahbgdc"], True),
    (["b", "abc"], True),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)