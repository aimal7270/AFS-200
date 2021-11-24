from datetime import datetime

name = input('Enter your name: ')
age = int(input('Enter your age: '))

year = ((datetime.now().year) - age) + 100

print("Hi " + name + ", you are ", age, "years old, and will turn 100 years old in ", year)