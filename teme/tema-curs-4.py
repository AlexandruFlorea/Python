# numero 1 - recursive sum function for undefined list of elements
def sum_function(*args, **kwargs):
    result = 0
    list_args = list(args) + list(kwargs.values())

    for item in list_args:
        if type(item) in [int, float]:
            result += item
        elif type(item) in [list, tuple, set]:
            result += sum_function(*item)

    return result


print(sum_function(2, 'adf', 4, 3.17, [1, 2, [2, (2, 1), {2, "asjhkad", 1}, 4.3], 5.13], fire=3, earth=[5, 2]))


#########################################################################
# numero 2 - recursive function
def complex_sum_function(n):
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = complex_sum_function(n - 1)
    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


t, e, o = complex_sum_function(5)
print(t, e, o)


########################################################################
# numero 3 - integer check
def is_integer():
    user_input = float(input('Enter the number you want to check: '))
    if user_input % 2 == 0:
        print(f"{user_input: .0f}")
    else:
        print(0)
