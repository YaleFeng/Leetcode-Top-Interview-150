from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_dict = {}
        for i in range(len(pattern)):
            value = pattern_dict.get(pattern[i], words[i])
            if value != words[i]:
                return False
            pattern_dict[pattern[i]] = value
        return len(set(pattern_dict.keys())) == len(set(pattern_dict.values()))
    
    
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.wordPattern(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["abba", "dog cat cat dog"], True),
    (["abba", "dog cat cat fish"], False),
    (["aaaa", "dog cat cat dog"], False),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)