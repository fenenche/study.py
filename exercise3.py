def list_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
my_list = [2, 4, 6, 8]
print(list_sum(my_list))