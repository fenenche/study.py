def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros_count = len(numbers) - len(non_zeros)
    return non_zeros + [0] * zeros_count
my_list = [1, 2, 3]
print(move_zeros(my_list))