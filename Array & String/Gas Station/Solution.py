from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        supply = sum(gas)
        demand = sum(cost)
        if supply < demand:
            return -1
        start_index = 0
        current_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1
        return start_index
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.canCompleteCircuit(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (([1,2,3,4,5], [3,4,5,1,2]), 3),
    (([2,3,4], [3,4,3]), -1),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)