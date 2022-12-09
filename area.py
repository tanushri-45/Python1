'''tem = eval(input("Enter the temprature in celsius"))
ce = 9/5*tem+32
print("Temprature in fahrenhiet is:", ce)'''

import math
mass = eval(input("Enter your mass"))
height = eval(input("Enter your height"))
bmi = mass/height**2
print("Your body mass index is:", bmi)

a = eval(input("Enter the first number"))
b = eval(input("Enter the second number"))
c = eval(input("Enter the third number"))
root1 = (-b+math.sqrt(b**2-4*a*c))/2*a
root2 = (-b-math.sqrt(b**2-4*a*c))/2*a
