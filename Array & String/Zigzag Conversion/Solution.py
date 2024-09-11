from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows >= len(s)) | (numRows == 1):
            return s
        order = []
        for i in range(1, 2*numRows - 1):
            if i <= numRows:
                order.append(i)
            else:
                order.append(numRows - (i - numRows))
        if len(s) % len(order) == 0:
            index = order * (((len(s) + 1) // numRows) - 1) + order
        else:
            print(len(s) % numRows)
            index = order * (((len(s) + 1) // numRows) - 1) + order[:(len(s) % len(order))]
        letter = [[] for _ in range(numRows)]
        for i in range(len(s)):
            letter[index[i] - 1].append(i)
        result = ''
        for i in range(numRows):
            for j in letter[i]:
                result += s[j]
        return result
        
# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.convert(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (["PAYPALISHIRING", 3], "PAHNAPLSIIGYIR"),
    (["PAYPALISHIRING", 4], "PINALSIGYAHRPI"),
    (["AB", 2], "AB"),
    (["A", 1], "A"),
    (["ABC", 2], "ACB"),
    (["ABCD", 3], "ABDC"),
    (["ABCDE", 2], "ACEBD"),
    (["PAYPALISHIRING", 6], "PRAIIYHNPSGAIL"),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)