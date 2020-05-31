print("*"*60)
print("INSTRUCTIONS")
print("Enter h if you want me to guess higher\n"
"Enter l if you want me to guess lower\n"
"Enter c if I have guessed it correctly\n")
print("*"*60)
valid_attempts=10
low = 1
high = 1000
print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER(mandatory) to start: ")

guesses = 1

while guesses <= valid_attempts:
    guess = low + (high - low)//2
    high_low= input("My guess is {}. Should I guess higher or lower? :- ".format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess -1
    elif high_low == "c":
        print("I guessed {0} in {1} attempt(s).".format(guess,guesses))
        break
    else:
        print("Please enter h, l or c only")
        guesses -=1 #if code goes here, we dont have to increase the guesses count.
    guesses +=1
    if guesses <= valid_attempts:
        continue
    else:
        next_input=input("Round 1 :- Attempts Over, Want to play again? [y or n] ").casefold()
        if next_input=="y":
            guesses=1
            low=1
            high=10
            while guesses <= valid_attempts:
                guess = low + (high - low)//2
                high_low= input("My guess is {}. Should I guess higher or lower? :- ".format(guess)).casefold()
                if high_low == "h":
                    low = guess + 1
                elif high_low == "l":
                    high = guess -1
                elif high_low == "c":
                    print("I guessed {0} in {1} attempt(s).".format(guess,guesses))
                    break
                else:
                    print("Please enter h, l or c only")
                    guesses -=1 #if code goes here, we dont have toincrease the guesses count.
                guesses +=1
            if guesses <= valid_attempts:
                continue
            else:
                print("You have used maximum number of attempts,See you again!!!")
                break
        else:
            print("Thanks for playing, see you soon")
    
    