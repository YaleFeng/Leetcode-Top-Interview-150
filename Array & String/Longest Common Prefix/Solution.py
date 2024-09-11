from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.longestCommonPrefix(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)