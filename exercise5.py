def count_occurences(numbers, target):
    occurences = 0
    for num in numbers:
        if num == target:
            occurences += 1
    return occurences
my_list = count_occurences(numbers = [2, 5, 2, 8, 2], target = 2)
print(my_list)