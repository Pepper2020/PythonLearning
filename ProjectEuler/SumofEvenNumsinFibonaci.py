
my_value1 = 1
my_value2 = 2
value_f = 1
sum_f = my_value2
while value_f <= 4000000:
    value_f = my_value1 + my_value2
    my_value1 = my_value2
    my_value2 = value_f
    if value_f % 2 == 0:
        sum_f += value_f

print(sum_f)
    
