from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            result = numbers[i] + numbers[j]
            if result == target:
                return [i + 1, j + 1]
            elif result > target:
                j -= 1
            else:
                i += 1
    

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.twoSum(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (([2,7,11,15], 9), [1, 2]),
    (([-1, 0], -1), [1, 2]),
    (([2,3,4], 6), [1, 3]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)