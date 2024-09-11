from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]
        for index, value in enumerate(citations):
            if value > n:
                temp[n] += 1
            else:
                temp[value] += 1
        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i


# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.hIndex(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([3,0,6,1,5], 3),
    ([1,3,1], 1),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)