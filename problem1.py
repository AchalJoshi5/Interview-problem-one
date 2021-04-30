#Write Python code to find if all the numbers in a given list of 
#integers are part of the series defined by the following. 
#f(0) = 0 f(1) = 1 f(n) = 9*f(n-1) - 4*f(n-2) for all n > 1. 
#def is_part_of_series(lst):

result = {}
def series(n):
    if n == 0:
        result[n] = 0
        return 0
    elif n == 1:
        result[n] = 1
        return 1
    else:
        val = 9*series(n-1)-4*series(n-2)
        result[n] = val
        return val

series(10)
lst = sorted(set(result.values()))
lst1 = range(100)


def is_part_of_series(lst, lst1):
    for x in lst:
        if x in lst1:
            print(x)

is_part_of_series(lst, lst1)



