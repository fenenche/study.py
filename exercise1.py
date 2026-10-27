def find_largest(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
my_list = [3, 41, 56, 21, 76, 9]
print(find_largest(my_list))