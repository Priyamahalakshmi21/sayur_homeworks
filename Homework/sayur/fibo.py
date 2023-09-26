max_num = int(input("Enter the maximum number in the Fibonacci sequence: "))
num1, num2 = 0, 1
print("Fibonacci sequence up to", max_num, ":")
print(num1, end=", ")
print(num2, end=", ")
for _ in range(max_num):
    fib = num1 + num2
    if fib > max_num:
        break
    print(fib, end=", ")
    num1, num2 = num2, fib
print()  