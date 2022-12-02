from time import perf_counter

base = 25 
power = 123123 
modulo = 2312 

start = perf_counter()
for _ in range(1000):
    base * power % modulo
print(f"01 Elapsed time: {perf_counter() - start}")

start = perf_counter()
for _ in range(1000):
    pow(base, power, modulo)
print(f"02 Elapsed time: {perf_counter() - start}")



# 01 Elapsed time: 0.000277623999863863
# 02 Elapsed time: 0.0022509089903905988