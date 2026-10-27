def reverse_list(items):
    reverse_items = []
    for i in range(len(items) -1, -1, -1):
        reverse_items.append(items[i])
    return reverse_items

my_list = [1, 2, 3, 4]
print(reverse_list(my_list))
