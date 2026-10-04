count = 0
number = 2

while count < 10:
    is_prime = True
    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number)
        count += 1

    number += 1
