from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        initial = nums[0]
        available = nums[1:(initial + 1)]
        index_list = list(range(1, len(available) + 1))
        if len(nums) == 1:
            return True
        while len(available) > 0:
            if len(index_list) == 0:
                return False
            if index_list[-1] >= (len(nums) - 1):
                return True
            drop = available.pop(0)
            new_index = [num for num in list(range((index_list[0] + 1),(index_list[0] + drop + 1))) if num > index_list[-1]]
            if len(new_index) > 0:
                available = available + nums[new_index[0]: new_index[-1] + 1]
                index_list = index_list + new_index
            index_list.pop(0)
        return False
    
        ### Good Answer
        
        # gas = 0

        # for n in nums:
        #     if gas < 0:
        #         return False
        #     if n > gas:
        #         gas = n
        #     gas -= 1 

        # return True


# Create instance of Solution class
solution = Solution()

def run_test_case(inputs, expected):
    output = solution.canJump(inputs)
    print(f"Testing with inputs: {inputs}")
    print(f"Expected: {expected}, Got: {output}")
    assert output == expected, f"Test failed for inputs {inputs}"
    print("Test passed!")

# Example test cases
test_cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([0], True),
    ([2,0], True),
    ([1,1,1,0], True),
    ([1,1,2,2,0,1,1], True)
]

# Run test cases
for inputs, expected in test_cases:
    run_test_case(inputs, expected)