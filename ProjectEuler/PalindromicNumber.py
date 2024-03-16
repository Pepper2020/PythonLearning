def is_palindromic(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        return True
    return False

def largest_palindromic(digit, step):
    step_value = int(step)
    limit = max_number_in_digits(digit)
    factor_one = limit - 1
    factor_two = 0
    total_loop = int(limit / step_value)
    for ind in range(0, total_loop):
        for m in range(0, step_value):
            for n in range(m, step_value):
                factor_one = limit - m
                factor_two = limit - n - ind * step_value
                num = factor_one * factor_two
                if is_palindromic(num):
                    print(f"Found a palindromic, factor one is {factor_one}, factor two is {factor_two}, the product {num} is palindromic.")
                    return num
                else:
                    print(f"Factors {factor_one} and {factor_two}, the product {num} is not palindromic.")
                    

            

def max_number_in_digits(digit):
    base = 1
    for ind in range(0, int(digit)):
        base *= 10
    print(f"limit number is {base - 1}")
    return base - 1

if __name__ == "__main__":
    num = input("Type the digit of the factor ==> ")
    step = input("Type the check step ==> ")
    print(f"The largest palindrome made from the product of two {num}-digit numbers is {largest_palindromic(num, step)}")