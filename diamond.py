#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines
lines = int(input("Enter number of lines: "))
number = 1
while number <= lines:
    space_input = input("Press the spacebar to print $ ")
    if space_input == " ":
        print(' ' * (lines - number), end='')
        print('$ ' * number)
        number += 1
    else:
        print("Exiting the program.")
        break

number -= 2  
while number >= 1:
    space_input = input("Press the spacebar to print $ ")
    if space_input == " ":
        print(' ' * (lines - number), end='')
        print('$ ' * number)
        number -= 1
    else:
        print("Exiting the program.")
        break