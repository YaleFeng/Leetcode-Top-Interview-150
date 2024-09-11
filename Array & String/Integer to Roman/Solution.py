from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        index = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        counts = {}
        for key, value in index.items():
            count = num // value
            counts[key] = count
            num = num - (count) * value
        result = ''
        for key, value in counts.items():
            result += value * key
        return result

# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.intToRoman(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (3749, "MMMDCCXLIX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)