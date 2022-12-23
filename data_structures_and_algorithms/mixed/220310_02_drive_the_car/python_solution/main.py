# https://practice.geeksforgeeks.org/problems/drive-the-car2541/1/

# --------------------- #



class Solution:
    def required(self, arr, N, K):
        extra_fuel = 0
        for i in range(N):
            if arr[i] > K:
                diff_fuel = arr[i] - K
                
                if diff_fuel > extra_fuel:
                    extra_fuel = diff_fuel

        if extra_fuel == 0:
            return -1
        else:
            return extra_fuel

# test 1 ------------------- #

N = 5
K = 7
arr = [2, 5, 4, 5, 2]
out_exp = -1

sol_inst = Solution()
print(sol_inst.required(arr, N, K) == out_exp) 


# test 2 --------------------- #
N = 5
K = 4
arr = [1, 6, 3, 5, 2]
out_exp = 2

sol_inst = Solution()
print(sol_inst.required(arr, N, K) == out_exp) 
