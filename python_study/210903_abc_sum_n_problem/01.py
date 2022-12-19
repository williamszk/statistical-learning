"""
https://www.youtube.com/watch?v=Q_1M2JaijjQ&ab_channel=Reducibl

given n a positive integer
find all the combinations of (a, b, c) that added gives n
find all (a, b, c) in such a way that a + b + c = 

two solutions
first naive, try all combinations of a, b, 
second, find all combinations of a, b where c is the by produc

measure the time of excution
where n is in the x axis and time in the y axis
"""
#%%

import time

import pandas as pd
import numpy as np


#%%

def time_it(func):
    """This higher order function will output the mean time elapsed execute another 
    function.
    """
    def outer_func(*args, **kwargs):
        list_times = []
        for i in range(2):
            t0 = time.time()
            func(*args, **kwargs)
            t1 = time.time()
            elapsed_time = t1 - t0
            list_times.append(elapsed_time)

        return np.mean(list_times)
    return outer_func

@time_it
def solution_01_find_abc_sum(n):
    list_answers = []
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                if a + b + c == n:
                    list_answers.append((a,b,c))

    return list_answers

#%%
n = 20
solution_01_find_abc_sum(n)
#%%
list_execs = []
for n in range(1, 1000):
    list_execs.append({
        "n":n,
        "time_exec":solution_01_find_abc_sum(n)
    })

#%%
df_time_exec = pd.DataFrame(list_execs)
df_time_exec.index = df_time_exec["n"]
df_time_exec["time_exec"].plot()
#%%


















