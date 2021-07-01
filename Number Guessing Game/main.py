import random
start_range = int(input('Enter a start number: '))
end_range = int(input('Enter a end number: '))
number = random.randint(start_range,end_range)
tries = 0
guess = 0
while guess != number:
    guess = int(input('Enter a guess: '))
    tries+=1
    if guess > number:
        print('The number is smaller!')
    else:
        print('The number is larger!')
    if guess == number:
        print(f' The number was {number} ,you won in {tries} tries!')