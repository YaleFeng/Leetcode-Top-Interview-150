from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        available = []
        for i in range(len(nums)):
            if (i > 0) & (nums[i] == nums[i - 1]):
                continue
            j = i + 1
            k = len(nums) - 1
            if j >= k:
                return available
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                if result == 0:
                    available.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while (nums[j] == nums[j - 1]) & (j < k):
                        j += 1
                elif result > 0:
                    k -= 1
                else:
                    j += 1
        return available

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.threeSum(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)