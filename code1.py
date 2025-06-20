
#question1

list=[12,15,18,23,22,27,26]
for x in list:
    if(x%2==0):
        print(x,"is even")
    else:
        print(x,"is odd")





#question2(else)


for i in range(1,4):
    print(i,"checked")
    i+=1
else:
    print(i+1,"not checked")



#question 3(nest)

num=int(input("enter:"))
if num>10:
    print(num," is greater than 10")
    if num>20:
        print(num, "is greater than 20")
else:
    print(num,"is less than 10")


#question4(multiple conditions)
age=int(input("please enter your age: "))
has_license=str(input("please enter whether you have license(yes/no): ")).strip().lower()
if age>=18 and has_license == "yes":
        print("legal driver")

elif age<18 and has_license == "yes":
    print("illegal driver")

elif age>18 and has_license == "no":
    print("illegal driver")

else:
    print("enter valid input")

#question5


ages=[78,34,21,34,12,9,4]
condition = True
if condition:
    print("ages 18 and above:")
    for age in ages:
        if age>=18:
            print(age)
            continue
    else:
        print("ages below 18")
        for age in ages:
            if age<18:
                print(age)

#factorial

num = int(input("enter a number"))
factorial = 1

if n>= 0:
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
else:
    print("Factorial does not exist for negative numbers")


#factorial using recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Factorial is", factorial_recursive(5))

#fibanocci

a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    next_term = a +b
    a=b
    b=next_term









            
    
        
