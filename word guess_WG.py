import random
number = random.randint(0,3)
words = ["cube","cap","money","map"]
hint1 = ["rubiks","hat","secret to happiness","lost"]
hint2 = ["shape","baseball","Everybody wants it","confusing"]
guess = ""
counter = 1
secretword = words[number]

while True:
    print("guess the secret word")
    print("type 'hint1', 'hint2', 'first letter','last letter', or 'give up'for help.")
    guess = input()
    if guess == secretword:
         print ("you win!")
         print ("you took " +str(counter) + " guesses")
         break
    elif guess == "hint1":
        print( hint1[number] )
    elif guess == "hint2":
        print( hint2[number] )
    elif guess == "first letter":
        print (secretword[0])
    elif guess == "last letter":
        print (secretword[-1])
    elif guess == "give up":
        print("the word was" + secretword)
        break
    else:
        print("try again.")
        counter += 1
