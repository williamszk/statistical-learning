# https://leetcode.com/problems/median-of-two-sorted-arrays/

#%%
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_join = nums1 + nums2 
        list_join.sort()
        len_list = len(list_join)
        if len_list % 2 == 0:
            median = (list_join[int(len_list / 2 -1)] + 
                     list_join[int(len_list / 2)]) / 2
        else:
            median = list_join[int((len_list - 1) / 2)]
        
        return median

#%%
nums1 = [1,3]
nums2 = [2]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2) == 2

#%%
nums1 = [1,2]
nums2 = [3,4]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2) == 2.5
#%%
nums1 = [0,0]
nums2 = [0,0]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2) == 0
#%%
nums1 = []
nums2 = [1]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2) == 1

#%%

