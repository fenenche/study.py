def find_number(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1      
my_list = find_number(numbers = [10, 25, 30, 45], target = 30)
print(my_list)