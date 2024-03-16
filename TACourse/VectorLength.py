
my_vector = (3, 5.23, 2.1532)
length = (my_vector[0] ** 2 + my_vector[1] ** 2 + my_vector[2] ** 2) ** 0.5
var_output1 = 'The length of vector ' + str(my_vector) + ' is ' + str(length)
print(var_output1)


x = float(input('Please input the x value of your vector2 --> '))
y = float(input('Please input the y value of your vector2 --> '))
z = (x ** 2 + y ** 2) ** 0.5
var_output2 = 'The length of vector (' + str(x) + ', ' + str(y) + ') is ' + str(z)
print(var_output2)