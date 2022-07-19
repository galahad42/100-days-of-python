n = int(input("Enter a number to check: "))

def is_prime(num):
    count = 0
    for i in (1, num):
        if num%i == 0:
            count += 1

        else:
            continue

    if count == 1:
        print(f"{num} is prime number")

    else:
        print(f"{num} is not a prime number")


is_prime(n)

