from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return (k, nums[:k])

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.removeDuplicates(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([1,1,2], (2, [1,2])),
    ([0,0,1,1,1,2,2,3,3,4], (5, [0,1,2,3,4])),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)