def name(firstName,age):
    print("Your name is" + firstName + "and you are " + str(age) + " years old.")
name(firstName=" Lilly ",age= 16 )

def addition(firstNumber,secondNumber):
    print(firstNumber + secondNumber)
addition(firstNumber=12,secondNumber=6)

def subtraction(firstNumber,secondNumber):
    print(firstNumber - secondNumber)
subtraction(firstNumber=20,secondNumber=5)

def multiplication(firstNumber,secondNumber):
    print(firstNumber * secondNumber)
multiplication(firstNumber=6,secondNumber=8)

def division(firstNumber,secondNumber):
    if secondNumber == 0:
        print("You can't divide a number by zero.")
    else:
        print(firstNumber / secondNumber)
division(firstNumber=10,secondNumber=2)
division(firstNumber=10,secondNumber=0)

#while loop
n = 0
while n < 5:
    print(n)
    n = n + 1

a = 5
while a != 0:
    print(a)
    a = a - 1
    
#for loop
flowers=["daisy", "rose", "lily", "buttercup"]
for x in flowers:
    print(x)

number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

for b in number:
    if b%3==0:
        if b%5==0:
            print("FizzBuzz")
        else:print("Fizz")
    elif b%5==0:
        print("Buzz")
    else:
        print(b)

num1=int(input("Please enter your first number"))
num2=int(input("Please enter your second number"))
num3=int(input("Please enter your third number"))

if num1 > num2:
    if num1 > num3:
        print(num1)
    elif num1 == num3:
        print("The two largest numbers are equal to", num3)
    else:
        print(num3)
elif num1 == num2:
    if num1 == num3:
        print ("The number are all equal to ", num1)
    elif num3 > num1:
        print(num3)
    else:
        print("The two largest numbers are equal to ", num1)
else:
    if num2 > num3:
        print(num2)
    elif num2 == num3:
         print("The two largest numbers are equal to ", num2)
    else:
        print(num3)
       
           
    
