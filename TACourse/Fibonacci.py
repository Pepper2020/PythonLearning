
def get_sum_of_fibonacci(max_ind) :
    try:
        my_value1 = 1
        my_value2 = 2
        index = 0
        while index < int(max_ind):
            temp = my_value1 + my_value2
            my_value1 = my_value2
            my_value2 = temp
            index += 1
        return my_value2
    except ValueError as ve:
        print("Function requires a number to proceed.")
        print(ve)

if __name__ == "__main__":
    #only print the result if this is the main program
    print("Sum of the first 10,000 numbers in a Fibonacci sequence is: ")
    print(get_sum_of_fibonacci(10000))