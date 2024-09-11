from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jump = 0
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            jump += 1

        return jump


# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.jump(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
    ([0], 0),
    ([2,0], 1),
    ([1,1,1,0], 3),
    ([1,1,2,2,0,1,1], 5)
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)