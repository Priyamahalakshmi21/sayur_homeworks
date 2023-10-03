# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
import random
computerNo = random.randint(1, 100)  
attempt = 0
while True:
    userNo = int(input("Guess the number: "))  
    attempt += 1
    if userNo < computerNo:
        print("Low")
    elif userNo > computerNo:
        print("High")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
print("User guessed the number in", attempt, "attempts")
