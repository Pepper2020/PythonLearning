def get_sum_of_odd_nums_in_fibonacci(upper_limit):
    my_value1 = 1
    my_value2 = 2
    value_f = 1
    sum_f = my_value2
    while value_f <= upper_limit:
        value_f = my_value1 + my_value2
        my_value1 = my_value2
        my_value2 = value_f
        if value_f % 2 == 1:
            sum_f += value_f
    return sum_f

if __name__ == "__main__":
    print(f'The sum of odd numbers lower than one million is: {get_sum_of_odd_nums_in_fibonacci(10000)}')
    
