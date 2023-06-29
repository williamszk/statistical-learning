"""Experiment with lambda expressions in python copying the functionality from
FormatList.hs
"""
# to run this write:
# python3 format_list.py


main = lambda:(
    print(f(2)),\
    print(format_list("<list>")("</list>")("|")(["first","second","third"])),\
    print("hello word"),\
    print(format_list_2("<list>","</list>","|",["first","second","third"]))
)

f = lambda x: x**2

format_list = lambda start: lambda end: lambda separator: lambda xs: start + f"{separator}".join(xs) + end
# format_list(start: str) -> (
#   func(end: str) -> (
#       func(separator)->(
#           func(xs)->str
#       )
#   )
# )

# in lambda we can define multiple arguments for the function
format_list_2 = lambda start, end, separator, xs: start + f"{separator}".join(xs) + end

if __name__ == "__main__":
    main()
