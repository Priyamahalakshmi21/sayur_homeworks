'''
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold
'''
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0, 0
while totalSales < 10000 and totalBagsSold < 10:
    print(f"Red Bags: {redBags}, White Bags: {whiteBags}")
    color = input("Enter the bag color (red/white): ")
    if color != 'red' and color != 'white':
        print("Invalid color. Please choose 'red' or 'white'.")
        continue
    quantity = int(input(f"Enter the quantity of {color} bags to buy: "))
    if color == 'red' and quantity > redBags:
        print("Sorry, we don't have enough red bags.")
        continue
    elif color == 'white' and quantity > whiteBags:
        print("Sorry, we don't have enough white bags.")
        continue
    if color == 'red':
        cost = quantity * 1000
        redBags -= quantity
    else:
        cost = quantity * 1500
        whiteBags -= quantity
    totalSales += cost
    totalBagsSold += quantity
print(f"Total Sales: Rs {totalSales}")
print(f"Total Bags Sold: {totalBagsSold}")