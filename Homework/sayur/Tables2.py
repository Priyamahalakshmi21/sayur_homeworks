#Print multiplication tables from 7 to 16, each number upto 12 rows.
for i in range(7, 17):  
    print(f"Multiplication table for {i}:")
    for j in range(1, 13):  
        result = i * j
        print(f"{j} x {i} = {result}")
    print() 
