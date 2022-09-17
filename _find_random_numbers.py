from mimetypes import guess_all_extensions
import random
rando =  random.randint(1,100)
print(rando)
userGuess=None
guesses =0

while(userGuess != rando):
    userGuess=int(input("Enter the right guess number to win "))
    guesses +=1
    if  userGuess == rando:
        print("You WON!!")
    elif userGuess < rando:
        print("guess greater number") 
    elif userGuess > rando:
        print("guess smaller number") 
print(f"you guessed the number in {guesses} guesses")
 
