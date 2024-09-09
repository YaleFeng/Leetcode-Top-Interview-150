from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 1
        same = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                same += 1
            else:
                same = 1
            if same < 3:
                nums[k] = nums[i]
                k += 1
        return (k, nums[:k])
    
        # k = 1
        # twice_list = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         continue
        #     if (nums[i] != nums[i - 1]):
        #         nums[k] = nums[i]
        #         k += 1
        #     if (nums[i] == nums[i - 1]) & (nums[i] not in twice_list):
        #         twice_list.append(nums[i])
        #         nums[k] = nums[i]
        #         k += 1

        # return (k, nums[:k])


# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.removeDuplicates(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([1,1,1,2,2,3], (5, [1,1,2,2,3])),
    ([0,0,1,1,1,1,2,3,3], (7, [0,0,1,1,2,3,3])),
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)