def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
my_list = [1, 2, 3, 4, 6]
print(count_even(my_list))