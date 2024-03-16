import Fibonacci as f

if __name__ == "__main__":
    print("This is main")
    user_input = input("The maximum number of this fibonaci sequence: ")
    print(f.get_sum_of_fibonacci(user_input))