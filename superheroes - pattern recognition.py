correct="no"
print("Please choose one of the following: The Flash, Wonder Woman, Iron Man or Black Widow.")
while correct != "yes":
    print("Is your chosen superhero from the marvel universe?")
    question1=input("Please enter yes or no.")
    if question1 == "yes":
        print("Does your chosen superhero use a super suit?")
        question2=input("Please enter yes or no.")
        if question2 == "yes":
            print("You have chosen Iron Man.")
            correct=input("Is this correct (yes, no)?")
        else:
            print("You have chosen Black Widow.")
            correct=input("Is this correct (yes, no)?")
    else:
        print("Does your chosen superhero have the power of super speed?")
        question3=input("Please enter yes or no.")
        if question3 == "yes":
            print("You have chosen The Flash.")
            correct=input("Is this correct (yes, no)?")
        else:
            print("You have chosen Wonder Woman.")
            correct=input("Is this correct (yes, no)?")
        
