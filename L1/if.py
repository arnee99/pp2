num = int(input('Enter any number: '))
print(type(num))
if (num % 5 == 0):
    print(f'Given number {num} is divisible by 5')
    print('This statement belongs to if statement')
print('This statement does not belongs to if statement')