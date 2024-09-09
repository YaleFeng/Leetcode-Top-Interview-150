from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy_p:
                buy_p = prices[i]
            profit = max(profit, prices[i] - buy_p)
        return profit

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.maxProfit(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([2,4,1], 2),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)