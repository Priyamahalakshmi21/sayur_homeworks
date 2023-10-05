'''
#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

  1  2  3  4  5
********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25
'''
start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))
print(" ", end=" ")  
for i in range(start_num, end_num + 1):
    print(i, end=" ")
print("\n" + "*"*15)
for i in range(start_num, end_num + 1):
    print(i, "|", end=" ")
    for j in range(start_num, end_num + 1):
        result = i * j
        print(result, end=" ")
    print()