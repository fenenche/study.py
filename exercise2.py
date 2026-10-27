def find_smallest(numbers):
    if not numbers:
        return None
    smallest_num = numbers[0]
    for num in numbers:
        if num < smallest_num:
            smallest_num = num
    return smallest_num
my_list = [8, 3, 12, 1, 7]
print(find_smallest(my_list))