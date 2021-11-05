
import random
number = random.randint(0,100)
while_sabiti = True
while while_sabiti:
    guess=int(input("Please enter your number:"))
    if guess > number:
        print("Please decrease your number!")
    elif guess < number:
        print("Please increase your number!")
    elif guess == number:
        print("Congratulations! number was {}".format(number))
        while_sabiti = False




