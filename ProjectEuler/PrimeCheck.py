def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print(f"Number 2345 is prime: {is_prime(int(2345))}")
    print(f"Number 3745 is prime: {is_prime(int(3741))}")
