#%%
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time complexity O(n²)
        """
        
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if a + b == target and a != b:
                    return [i,j]




#%%
# find a solution more efficient than O(n²) time complexity

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time complexity: idk
        
        """
        len_list = len(nums)
        list_idx = list(range(len_list))
        for i in list_idx:
            a = nums[i]
            for j in list_idx[i+1:]:
                b = nums[j]
                if a + b == target:
                    return [i, j]


#%%

nums = [2,7,11,15]
target = 9

expected_output = [0,1]

solution = Solution()
print(solution.twoSum(nums, target))


# %%
