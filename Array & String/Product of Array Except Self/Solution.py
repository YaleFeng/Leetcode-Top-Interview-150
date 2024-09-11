from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_include = 0
        result = [0] * len(nums)
        for i in nums:
            if i == 0:
                zero_include += 1
                continue
            else:
                total *= i
        for i in range(len(nums)):
            if zero_include > 1:
                return result
            elif zero_include == 1:
                if nums[i] == 0:
                    result[i] = int(total)
            else:
                result[i] = int(total / nums[i])
        return result

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.productExceptSelf(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)