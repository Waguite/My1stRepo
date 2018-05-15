import random
import time

number = random.randint(1,100)
guess = 0
counter = 0
while True:
    print("guess my number between 1 and 100.")
    guess = int(input())
    counter += 1
    
    if guess == number:
        print("you win")
        print("you tried" + str(counter) + "guesses.")
        break
        
    elif guess > number:
        print("too high!")
        
    elif guess < number:
        print ("too low!")
