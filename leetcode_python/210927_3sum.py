# https://leetcode.com/problems/3sum/
#%%
from typing import List
import numpy as np

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_of_sums = []
        list_sets = []
        len_nums = len(nums)
        for i in range(0, len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    list_numbers = [nums[i], nums[j], nums[k]]
                    sum_three = np.sum(list_numbers) 
                    if sum_three == 0:
                        if len(list_of_sums) > 0:
                            list_sets = [set(x) for x in list_of_sums]

                        if not set(list_numbers) in list_sets:
                            list_of_sums.append(list_numbers)

        return list_of_sums

#%%
nums = [-1,0,1,2,-1,-4]
solution = Solution()
solution.threeSum(nums) == [[-1,-1,2],[-1,0,1]]
#%%
nums = []
solution = Solution()
solution.threeSum(nums) == []
#%%
nums = [0]
solution = Solution()
solution.threeSum(nums) == []
#%%

