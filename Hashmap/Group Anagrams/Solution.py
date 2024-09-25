from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_element = defaultdict(list)
        # word_element = {}
        for word in strs:
            key = "".join(sorted(word))
            # key = sorted(word)
            word_element[key].append(word)
        return word_element.values()
    
    
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.groupAnagrams(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
    ([""], [[""]]),
    (["a"], [["a"]]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)