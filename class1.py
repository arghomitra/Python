# this is a comment

"""
print("Hello World!")


first_name = "argho"
last_name = "mitra"
age = 21
# print(first_name + " "+last_name)
print("My first name is "+first_name)
birth_year = 2023-age
print(birth_year)

x = 5
if x > 0:
    print("x is a positive number")
elif x < 0:
    print("a negative number")
else:
    print("x is 0 ")

    x = input("enter a number")
    print(int(x)+5)
print(f"hello,{first_name}")

string = "hoW is lIFe"
name = input("name:")
print(string.lower())
print(string.replace(" ", "*"))


birthday = input("What is your birthDay?")
print(birthday.split("-"), "is your!")

age = input("how old are you?")
if age.isnumeric():
    age = int(age)
    if age < 12:
        print("no")
    elif (age <= 15):
        print("Don't drink much")
    else:
        print("enjoy")

else:
    print("your input was not a number")

for i in range(1, 10):
    print(i)

# for i in range(0, 100):
#     print(f"we are printing out {i+1}th time")

import datetime


def calculate_birthyear(age):
    return datetime.date.today().year - age


age = 21
birthday = calculate_birthyear(age)

print(f"if you were born in {birthday}, then your age is {age}")


import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))
"""
# password = "verysecure1"
# for i in password:
#     if (i.isalpha()):
#         print("yes")
#     elif (i.isdigit()):
#         print("num")
#     elif (i.isdigit()):
#         print("num")
#     elif (i.__contains__("1")):

#         print("1")


special = "@!$"
digit = "0123456789"
password = "verysecureU$"
# password = input("password:  ")

if any((c in special for c in password) and (c in digit for c in password) and ("password" not in password) and (("123456") not in password)):
    print("The password is valid!")
elif (c not in special for c in password):
    print("The password must contain at least one of the following special characters: $, @ or !")
# if any(c in digit for c in password):
#     print("YES")
elif (c not in digit for c in password):
    print("The password must contain at least digit character.")

if (password.startswith("qwerty") or (password.startswith("QWERTY"))):
    print("The password can't contain qwerty/QWERTY word.")

if ("password" in password):
    print("The password may not contain the keywords “password” or “123456”.")
if ("123456" in password):
    print("The password may not contain the keywords “password” or “123456”.")


"""
password = "verysecurea$"

is_upper = False
for i in password:
    if i.isupper():
        is_upper = True
        break

    else:
        is_upper = False
print(is_upper)
"""
