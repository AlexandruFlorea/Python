#
# # numero 1 - sum function var 1
# def sum_function(*numbers, **others):
#     result = 0
#     for number in numbers:
#         try:
#             int(number)
#             result += number
#             continue
#         except ValueError:
#             pass
#
#     return result


# print(sum_function(2, 'adf', 4, 3.17, fire=3))

# numero 1 - sum function var 2
def sum_function(*args, **others):
    result = 0
    for item in args:
        if isinstance(item, int) or isinstance(item, float):
            result += item
        elif isinstance(item, list):
            for list_item in item:
                result += list_item
    return result


print(sum_function(2, 'adf', 4, 3.17, [1, 2, 5.13], fire=3))


#########################################################################
# # numero 2 - recursive function
# def complex_sum_function(n):
#     number_list = list(range(n+1))
#     total_sum = 0
#     even_num_sum = 0
#     odd_num_sum = 0
#
#     for num in number_list:
#         total_sum += num
#         if num % 2 == 0:
#             even_num_sum += num
#         else:
#             odd_num_sum += num
#
#     return f"Sum of all numbers is {total_sum}\n" \
#            f"Sum of even numbers is {even_num_sum}\n"\
#            f"Sum of odd numbers is {odd_num_sum}"
#
#
# print(complex_sum_function(5))


########################################################################
# # numero 3 - integer check
# def is_integer():
#     user_input = float(input('Enter the number you want to check: '))
#     if user_input % 2 == 0:
#         print(f"{user_input: .0f}")
#     else:
#         print(0)
#
#
# is_integer()
