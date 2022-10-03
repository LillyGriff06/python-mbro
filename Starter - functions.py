def minutestoseconds():
    minutes= int(input("Please enter minutes."))
    seconds= minutes*60
    print("This is", seconds, "seconds.")
minutestoseconds()

def addition():
    num1= int(input("Please enter a number"))
    num2= int(input("Please enter a number"))
    total= num1 + num2
    print("The answer is", total)
addition()

def ageconversion():
    ageyears= int(input("Please enter age in years."))
    agedays= ageyears*365
    print("This is", agedays, "days.")
ageconversion()

def temperatureconversion():
    fahrenheit= int(input("Please enter the temperature in fahrenheit."))
    half= fahrenheit-32
    celsius= half/1.8
    print("This is", celsius, "degrees celsius.")
temperatureconversion()

flowers=["lily", "rose", "daisy", "poppy", "daffodil", "buttercup"]

print(flowers[0])
print(flowers[5])
print(len(flowers))

