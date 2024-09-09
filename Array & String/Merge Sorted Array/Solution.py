from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_index = m - 1
        n_index = n - 1
        total = (m + n) - 1

        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] > nums2[n_index]:
                nums1[total] = nums1[m_index]
                m_index -= 1
            else:
                nums1[total] = nums2[n_index]
                n_index -= 1
            total -= 1

        while n_index >= 0:
            nums1[total] = nums2[n_index]
            n_index -= 1
            total -= 1
            
        return nums1


# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.merge(*inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6]),
    (([1], 1, [], 0), [1]),
    (([0], 0, [1], 1), [1]),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)