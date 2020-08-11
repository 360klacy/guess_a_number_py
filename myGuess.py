import random
number = random.randint(1,10)
# print number

player_name = input("Whats good! Whats your first name?")

number_of_guesses = 0

print('I see you!' + player_name + 'I am guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low lil grasshopper')
    if guess >number:
        print('Your guess is too high lil grasshopper')
    if guess == number:
        break