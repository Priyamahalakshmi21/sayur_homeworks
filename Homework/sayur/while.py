no_of_Cake = 0
no_of_Chocolate = 0
money = int(input("Enter your budget: "))
while money >= 150:
    if money >= 200:
        no_of_Chocolate += 1
        money -= 200
    else:
        no_of_Cake += 1
        money -= 150
print("Number of chocolates bought:", no_of_Chocolate)
print("Number of cakes bought:", no_of_Cake)