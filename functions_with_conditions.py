def check_number(number):
    if number > 0:
        return "Positive number"
    else:
        return "Not a positive number"

answer = check_number(-5)
print(answer)




def check_number(number):
    if number > 0:
        return "Positive"
    else:
        return "Not positive"

print(check_number(10))
print(check_number(0))
print(check_number(-3))