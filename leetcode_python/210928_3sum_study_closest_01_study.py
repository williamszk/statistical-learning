# https://leetcode.com/problems/3sum-closest/
# https://leetcode.com/problems/3sum-closest/discuss/1490478/Python-with-2-pointers-approach
#%%
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return []
        
        # First sort the array (nlogn)
        nums = sorted(nums)
        
        closest_sum = None
        min_distance = None

        # For each element, search the pair that gets it closer to the target.
        for i in xrange(0, len(nums)-2):  #(nlogn)
            start = i+1
            end = len(nums) -1
            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                cur_distance = abs(target-cur_sum)
                
                if cur_sum == target:
                    return cur_sum
                
                if not min_distance or min_distance > cur_distance:
                    min_distance = cur_distance
                    closest_sum = cur_sum
                
                if cur_sum < target:
                    start += 1
                else:
                    end -= 1
                    
        return closest_sum
#%%
nums = [-1,2,1,-4]
target = 1
solution = Solution()
solution.threeSumClosest(nums, target) == 2

#%%

