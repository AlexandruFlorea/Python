#
# # numero 1 - sum function
def sum_function(*numbers, **others):
    numbers_to_add = []
    for number in numbers:
        try:
            int(number)
            numbers_to_add.append(number)
            continue
        except ValueError:
            pass

    return sum(numbers_to_add)

print(sum_function(2, 'adf', 4, fire=3))


# numero 2 - recursive function
def complex_sum_function(n):
    number_list = list(range(n+1))
    even_num_sum = []
    odd_num_sum = []

    for num in number_list:
        if num % 2 == 0:
            even_num_sum.append(num)
        else:
            odd_num_sum.append(num)


    def total_sum(n):
        if n == 0:
            return 0
        else:
            return n + total_sum(n - 1)
    total_sum(n)

    return f"Sum of all numbers is {total_sum(n)}\n" \
           f"Sum of even numbers is {sum(even_num_sum)}\n"\
           f"Sum of odd numbers is {sum(odd_num_sum)}"

print(complex_sum_function(5))
# Acu, vreau si varianta mai curata sau directa



# numero 3 - integer check
def is_integer():
    user_input = float(input('Enter the number you want to check: '))
    if user_input % 2 == 0:
        print(f"{user_input: .0f}")
    else:
        print(0)


is_integer()