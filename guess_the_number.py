import random

# It generates a random number between 0 and 100
number = random.randint(0, 100)

# Number of tries is set to 0
count = 0

input("Hey user, welcome to the Guess the Game")

# An while loop for less than 5 tries to guess the number
while count < 5:
    num = int(input("Please your guess between 1 to 100: "))

    if num > number:
        print("Man, man, man, man, holdup........ You are going too high. Guess a smaller number")
        # For each wrong answer,the count will increase by one
        count += 1

    elif num < number:
        print("Why are going too far away.... Guess a larger number")
        # For each wrong answer,the count will increase by one
        count += 1

    elif num == number:
        break


# The end messages, if he wins or loses
if num == number:
    print("congrats, you have guessed the right number")

else:
    print("Sorry,all your attempts in vain....... The right answer is " + str(number))