print("===== EXPENSE TRACKER =====")

expense = input("What did you buy? ")
amount = float(input("How much did it cost? "))

print("You bought:", expense)
print("You spent:", amount)

expense2 = input("What else did you buy? ")
amount2 = float(input("How much did it cost? "))

total = amount + amount2

print("Total spent:", total)
