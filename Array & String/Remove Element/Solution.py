from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return nums[:k]

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.removeElement(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (([3,2,2,3], 3), [2,2]),
    (([0,1,2,2,3,0,4,2], 2), [0,1,3,0,4]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)