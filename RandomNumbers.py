import random
 
secreteNumber = random.randint(1,100)
guesses =0
while True :
    guess = int(input("Please Enter a Guess :"))

    if guess > secreteNumber:   
        guesses +=1
        print("Please Guess Lowwer !!")
    elif guess < secreteNumber:
        guesses +=1
        print("Please Guess Higgher")
    else:
        print("Wow Your Guess Right")
        print(f"You Did it In : {guesses} guesses")
        break