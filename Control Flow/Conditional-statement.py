'''Write a simple python program that accepts user 
    input and checks if a number entered is Even or Odd'''

number = input("Enter a number: ")

if int(number) % 2 == 0:
    print("Even number")
else:
    print("Odd number")