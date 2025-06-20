#1
numbers = [10, 15, 23, 42, 56]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#2
for i in range(1, 4):
    print(f"i = {i}")
    if i == 5:
        break
else:
    print("Loop completed without break")


#3
x = 25
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")


#4
age = 22
has_license = True
if age >= 18 and has_license:
    print("You are allowed to drive")
else:
    print("You are not allowed to drive")



#5
ages = [78, 34, 21, 47, 9]
condition = True
for age in ages:
    if condition:
        print(f"Age {age} meets the condition")
    else:
        print(f"Age {age} does not meet the condition")



#6
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is {factorial}")



#7
n = 7
a, b = 0, 1
print("Fibonacci sequence:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



#8
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(7):
    print(fibonacci_recursive(i), end=" ")


#9
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(f"Factorial (recursive) of 5 is {factorial_recursive(5)}")
