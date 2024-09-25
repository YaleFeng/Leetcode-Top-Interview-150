from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_dict = {}
        for i in range(len(s)):
            word_dict[s[i]] = 1 + word_dict.get(s[i], 0)
        for i in range(len(t)):
            word_dict[t[i]] = word_dict.get(t[i], 0) - 1
            if word_dict[t[i]] < 0:
                return False
        return True
    
    
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.isAnagram(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["anagram", "nagaram"], True),
    (["rat", "car"], False),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)