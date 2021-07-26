initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
ascending_list = sorted(initial_list)
descending_list = sorted(initial_list, reverse=True) # descending_list = sorted(initial_list)[::-1]
even_numbers = ascending_list[1::2]
odd_numbers = ascending_list[::2]
multiples_of_3 = ascending_list[2::3]

print(initial_list, id(initial_list))
print(ascending_list, id(ascending_list))
print(descending_list, id(descending_list))
print(even_numbers)
print(odd_numbers)
print(multiples_of_3)