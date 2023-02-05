# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

from typing import List

value_items = [60, 100, 120]
weight_items = [10, 20, 30]

knapsack_capacity = 50

# Brute force solution

# the two arrays must have the same length



# we can make a solution using loop
# find all the combinations of itens that are less then knapsack_capacity

# we need to build a power_set
# Wladson book

def power_set(values: List) -> List[List]:
    """
    combination with no repetition
    we need at least 1 element
    values = [0, 1, 2, 3]
    """
    # are the values in the list unique? 
    values_2 = list(set(values))
    qtd_values = len(values_2)
    output_list = []

    # for item in values_2:
    #     output_list.append(list(item))
    
    for n_itens in range(1, qtd_values + 1):
        

        
        
        n_itens
    
def combinator(num_positions: int, itens: List) -> List[List]:
    """
    Given num_positions with num_itens
    find the combination (order is not important) without repetition.

    Example
    =======
    ```
    num_positions = 2
    itens = [0, 1, 2]
    0 1
    0 2
    1 2
    ```
    """

    for i in itens:
        pass












def f():
    max_value = 0

    while True:
        index = 0
        sum_weight = 0
        sum_value = 0

        while True:
            if sum_weight <= knapsack_capacity:
                sum_weight += weight_items[index]
                sum_value += value_items[index]
                
            else:
                pass


            index += 1
        
        break









# and another using recursion


#%%
# understanding implementation from geeksforgeeks

item_values = [60, 100, 120]
item_weights = [10, 20, 30]
num_itens = len(item_weights)

def knapsack(weight_capacity, item_weights, item_values, num_itens):
    """
    Returns the maximum capacity of the knapsack, given the
    arguments of the function.
    """
    
    # base case
    if num_itens == 0 or weight_capacity == 0:
        return 0
    
    # I think that first we need to sort the itens by weight
    # then pass them to the function
    if (weight_items[num_itens - 1] > weight_capacity):
        return knapsack(weight_capacity, item_weights, item_values, num_itens - 1)
    
    else:
        return max(
            item_values[num_itens - 1] + knapsack(weight_capacity - )

        )

# it is hard... maybe in the future I can understand
# this recursion seems to be sophisticated
# It seems that it can explore all possible combination of values
#%%



# I have 6 slots, 3 types of candy
# how combinations of candy configuration can I have?

# let there be candy 1, 2, 3
# 1 1 1 1 1 1 
# 1 1 1 1 2 3 = 2 1 1 1 1 3 = 1 1 2 1 1 3 = 3 1 1 1 1 2 
# so the position and order of the candy is not imporntat
# we can write:
# 1 1 1 1 | 2 | 3
# 1 1 1 | 2 2 | 3
# 1 1 | 2 2 2 | 3
# 1 | 2 2 2 2 | 3
# - | - - - - | -
# 
# this is a combinatorial problem with repetition
# notice that the important aspect of the problem
# is to change the position of | | in the 8 positions that we have
# the problem is 8 positions with 2 items with no repetition
#

# https://www.cs.sfu.ca/~ggbaker/zju/math/perm-comb-more.html#:~:text=Combinations%20with%20Repetition,-We%20can%20also&text=Same%20as%20other%20combinations%3A%20order,the%20same%20thing%20multiple%20times.





