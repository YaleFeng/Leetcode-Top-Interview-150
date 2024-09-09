from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]] += 1
            else:
                record[nums[i]] = 0
        return max(record, key=record.get)

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.majorityElement(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)