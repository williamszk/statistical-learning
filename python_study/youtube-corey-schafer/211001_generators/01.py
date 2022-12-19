# https://www.youtube.com/watch?v=bD05uGo_sVI&ab_channel=CoreySchafer
"""
The generator will not use the RAM memory all at once.
It will generate the necessary values each time when it is called.
"""
#%%
def square_numbers(nums):
    """Square all numbers of a list (nums).
    """
    results = []
    for i in nums:
        results.append(i*i)
    return results

#%%
nums = [1,2,3,4,5]
square_numbers(nums)
#%%
def square_numbers(nums):
    """Square all numbers of a list (nums).
    """
    for i in nums:
        yield (i*i)

# %%
nums = [1,2,3,4,5]
my_nums = square_numbers(nums)
my_nums
# %%
for i in my_nums:
    print(i)
# %%
# how to build generators with list comprehension syntax
nums = [1,2,3,4,5]
# use parenthesis
my_nums = (x**2 for x in nums)
nums
#%%
for i in my_nums:
    print(i)
# %%
# how to convert the values of a generator into a list?
my_nums = (x**2 for x in nums)
list(my_nums)
# %%


# %%


# %%


# %%


# %%


