from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        for i in range(len(s)):
            s_value = s_dict.get(s[i], t[i])
            if s_value != t[i]:
                return False
            s_dict[s[i]] = s_value
        return len(set(s_dict.keys())) == len(set(s_dict.values()))
    
    
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.isIsomorphic(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["egg", "add"], True),
    (["foo", "bar"], False),
    (["paper", "title"], True),
    (["badc", "baba"], False),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)