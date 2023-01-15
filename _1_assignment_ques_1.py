# Write a Python program to get the Fibonacci series between 0 to 50

num = int(input("Pls enter a number above 10: "))
print("Fibonacci series up to 50: ")

num1 = 0
num2 = 1

for i in range(num):
    print(num2, end=" ")

    next_num = num1 + num2
    if next_num > 50:
        break
    
    num1 = num2
    num2 = next_num

