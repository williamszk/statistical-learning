# https://leetcode.com/problems/3sum-closest/
#%%
from typing import List
import numpy as np

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        list_sums = []
        len_nums = len(nums)
        for i in range(0, len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    sum_3 = nums[i] + nums[j] + nums[k]
                    list_sums.append(sum_3)

        min_value = np.min([ np.abs(x - target) for x in list_sums])
        closest_sum = [x for x in list_sums if np.abs(x-target) == min_value][0]

        return closest_sum

        
#%%
nums = [-1,2,1,-4]
target = 1
solution = Solution()
solution.threeSumClosest(nums, target) == 2

#%%
nums = [0,0,0]
target = 1
solution = Solution()
solution.threeSumClosest(nums, target) == 0

#%%
nums = [-73,-26,10,-40,-74,81,20,-52,80,32,-17,-20,19,34,-2,94,-81,-66,-17,93,26,36,54,40,40,32,3,77,-30,14,-28,-74,-60,-99,11,0,-31,-84,90,-51,-29,87,-67,55,6,96,9,-76,75,-44,32,89,13,46,29,66,-12,-90,81,43,-46,54,74,22,70,-66,-43,97,93,-26,6,45,9,-64,-11,-43,-78,44,-92,98,-65,29,83,-30,35,-63,13,-92,-9,79,95,-44,50,55,87,-69,81,-91,-57,5,-9,65,42,11,78,-4,-43,10,1,0,50,-37,100,61,-82,-13,100,46,0,-25,13,16,43,49,92,31,85,38,-63,6,-30,67,64,-4,-71,-74,-92,6,-50,-45,-71,-82,11,-39]
target = 299
solution = Solution()
solution.threeSumClosest(nums, target)
# %%
