import PrimeCheck as p

def biggest_prime_factor(n):
    factor = 1
    for ind in range(n):
        if ind is not 0 and n % ind == 0:
            factor = n / ind
            if p.is_prime(factor):
                return factor
    return 0

if __name__ == "__main__":
    number = int(input("Type a number to get its biggest prime factor"))
    print(f"The biggest prime factor of {number} is {biggest_prime_factor(number)}")


# python
# Copy code
# import PrimeCheck as p
# import math

# def biggest_prime_factor(n):
#     max_prime = 1
#     # Check divisibility by 2
#     while n % 2 == 0:
#         max_prime = 2
#         n //= 2

#     # Check divisibility by odd numbers up to sqrt(n)
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             max_prime = i
#             n //= i

#     # If n is a prime greater than 2
#     if n > 2:
#         max_prime = n

#     return max_prime

# if __name__ == "__main__":
#     number = int(input("Type a number to get its biggest prime factor: "))
#     print(f"The biggest prime factor of {number} is {biggest_prime_factor(number)}")