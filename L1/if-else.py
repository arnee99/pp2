# Python code for testing whether a given number is Even or Odd
num = int(input('Enter any number : '))
if num % 2 == 0:
    print(f'The number {num} is a Even number')
elif num % 2 == 1:
    print(f'The number {num} is a Odd number')
else:
    print(f'Nothing!')