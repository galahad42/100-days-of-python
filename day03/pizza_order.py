from email.charset import add_charset


print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, L? ")
add_pepperoni = input("Do you want pepperoni? N, Y? ")
extra_cheese = input("Do you want extra cheese? N, Y? ")
error_msg = "Please type the correct response. "

if size == "S":
    s = 15
elif size == "M":
    s = 20
elif size == "L":
    s = 25
else:
    print(error_msg)

if extra_cheese == "Y":
    c = 1
elif extra_cheese == "N":
    c = 0
else:
    print(error_msg)

if add_pepperoni == "Y":
    if size == "S":
        p = 1
    else:
        p = 3
elif add_pepperoni =="N":
    p = 0
else:
    print(error_msg)

bill = s+c+p
print(f"\nYour final bill is: ${bill}")