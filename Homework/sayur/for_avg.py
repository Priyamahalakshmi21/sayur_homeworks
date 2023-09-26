total = 0
count = int(input("Enter the number of marks: "))
for i in range(count):
    mark = float(input("Enter a mark: "))  
    total += mark
if count > 0:
    average = total / count
    print("Average is", average)
else:
    print("No marks entered, so the average cannot be calculated.")