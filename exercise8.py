def has_duplicates(numbers):
    duplicates = set()
    for num in numbers:
        if num in duplicates:
            return True
            duplicates.add(num)
    for num in numbers:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False
my_list = []
print(has_duplicates(my_list))