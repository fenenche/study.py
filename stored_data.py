print("users email")
print("users password")

users_email = "favour12@.com"
users_password = "1234"

email = input("users email: ")
password = input("users password: ")

if email != users_email:
    print("account does not exist!")
elif password == users_password:
   print("login successful!")
else:
   print("incorrect password")


