# Question 1
name = input("What is your name: ")
age = input("How old are you: ")
print("hello " + name + " you are " + age + " years old")

# Question 2
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is: " + str(area))

# Question 3
temperature = float(input("What is the temperature in Celsius: "))
fahrenheit = (temperature * 9/5) + 32
print("The temperature in Fahrenheit is: " + str(round(fahrenheit, 2)))