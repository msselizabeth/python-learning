# regular function
def func(a, b, c=10):
    total = a + b + c
    return total

# calling by position and without c argument
print(func(2,3))
# calling by position and with provided agruments
print(func(2,3,5))
# calling by keys
print(func(c=2,a=3,b=5))


# function with variable number of parameters
def func1(a, *nums):
    '''Calc average.
   
    Parameters of the func:
    a - quantity 
    *nums - list of the nums
    total = sum of the num's items
    average - return value which equals total divides to a
    '''
    average = 0
    total = 0
    for n in nums:
        total += n
    average = total / a
    return average

print(func1.__doc__)
result = func1(3, 10,12,17)
print(f"{result:.2f}")
