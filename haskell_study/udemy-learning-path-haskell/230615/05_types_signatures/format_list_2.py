"""This time I'll just make an adjustment compared to format_list.py
"""
# to run this write:
# python3 format_list_2.py

def λ(x, func):
    return func(x)

print(λ([1,2,3], lambda xi: sum(xi)))

λ = lambda x, func: func(x)

print(λ([1,2,3], lambda xi: sum(xi)))

