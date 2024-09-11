from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        index = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            value = index[s[i]]
            if i != len(s) - 1:
                if index[s[i]] < index[s[i + 1]]:
                    num -= value
                else:
                    num += value
            else:
                num += value
        return num
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.romanToInt(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)