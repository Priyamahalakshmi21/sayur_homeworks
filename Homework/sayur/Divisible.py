number = int(input("Enter a number: "))
if number % 2 == 0 and (number % 3 == 0 and number % 5 == 0):
    print(f"{number} is divisible by 2,3,5")
elif number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 3,5.")
elif number % 5 == 0 and number % 2 == 0:
    print(f"{number} is divisible by 5,2.")
elif number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by 2,3.")
elif number % 2 == 0: 
    print(f"{number} is divisible by 2")
elif number % 3 == 0 :
    print(f"{number} is divisible by 3")
elif number % 5== 0 :
    print(f"{number} is divisible by 5")  
else:
    print(f"{number} is not divisible by 2,3,5.")