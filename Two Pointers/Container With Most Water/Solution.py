from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if current_area > max_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.maxArea(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
   ([1,1], 1),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)