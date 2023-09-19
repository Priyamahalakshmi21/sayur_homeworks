fruits_basket = input("Enter a list of fruits separated by commas: ")
fruits = [fruit.strip().lower() for fruit in fruits_basket.split(',')]
unique_fruits = set(fruits)
print("Unique Fruits:")
for fruit in unique_fruits:
    print(fruit.capitalize())