# https://leetcode.com/problems/4sum/
# %%
# solution based on:
# https://leetcode.com/problems/3sum-closest/discuss/1490478/Python-with-2-pointers-approach
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums can be nothing, None or a falsy value
        # it is not possible to calculate the sum of 4 distinct
        # items if we don't have at least 4 items to sum        
        if not nums or len(nums) < 4:
            output_list = []
        else:
            output_list = []
            current_list_set = []
            # first, sort the list
            nums = sorted(nums)

            for i, _num in enumerate(nums):
                start_1 = i + 1
                start_2 = i + 2
                end = len(nums) - 1

                while start_1 < start_2 < end:
                    current_list = [_num, nums[start_1], nums[start_2], nums[end]]
                    current_sum = sum(current_list)

                    if current_sum == target:
                        if not set(current_list) in current_list_set:
                            output_list.append(current_list)
                            current_list_set = [set(x) for x in output_list]
                        break

                    elif current_sum < target:
                        if start_2 - 1 == end:
                            start_1 += 1
                        else:
                            start_2 += 1
                    
                    else:
                        end -= 1

            # reverse sorted list
            nums = sorted(nums, reverse=True)
            for i, _num in enumerate(nums):
                start_1 = i + 1
                start_2 = i + 2
                end = len(nums) - 1

                while start_1 < start_2 < end:
                    current_list = [_num, nums[start_1], nums[start_2], nums[end]]
                    current_sum = sum(current_list)

                    if current_sum == target:
                        if not set(current_list) in current_list_set:
                            output_list.append(current_list)
                            current_list_set = [set(x) for x in output_list]
                        break

                    elif current_sum > target:
                        if start_2 - 1 == end:
                            start_1 += 1
                        else:
                            start_2 += 1
                    
                    else:
                        end -= 1            

        return output_list


# %%
nums = [1,0,-1,0,-2,2]
target = 0
expected_answer = [set(x) for x in [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]]
solution = Solution()
output_list = solution.fourSum(nums, target)
list_sets_answer = [set(x) for x in output_list]
all([x in expected_answer for x in list_sets_answer])

# %%
nums = [2,2,2,2,2]
target = 8
expected_answer = [set(x) for x in [[2,2,2,2]]]
solution = Solution()
output_list = solution.fourSum(nums, target)
list_sets_answer = [set(x) for x in output_list]
all([x in expected_answer for x in list_sets_answer])
# %%

# %%

# %%

# %%

# %%

# %%

# %%

