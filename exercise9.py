def first_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None
my_list = [5, 5, 3]

print(first_duplicate(my_list))