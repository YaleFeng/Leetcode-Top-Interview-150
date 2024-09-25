from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for c in magazine:
            mag_dict[c] = 1 + mag_dict.get(c, 0)
        for c in ransomNote:
            mag_dict[c] = mag_dict.get(c, 0) - 1
            if mag_dict[c] < 0:
                return False
        return True
    
    
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.canConstruct(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["a", "b"], False),
    (["aa", "ab"], False),
    (["aa", "aab"], True),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)