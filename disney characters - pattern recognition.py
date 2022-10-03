correct="no"
print("Please choose one of the following: Belle, Aurora, Ariel, Maleficent, Luz or Hunter.")
while correct != "yes":
    print("Does your chosen disney character have royal status?")
    question1=input("Please enter yes or no.")
    if question1 == "yes":
        print("Was your disney character born royal?")
        question2=input("Please enter yes or no.")
        if question2 == "yes":
            print("Is your chosen disney character from the sea?")
            question3=input("Please enter yes or no.")
            if question3 == "yes":
                print("You have chosen Ariel.")
                correct=input("Is this correct (yes, no)?")
            else:
                    print("You have chosen Aurora.")
                    correct=input("Is this correct (yes, no)?")
        else:
            print("You have chosen Belle.")
            correct=input("Is this correct (yes, no)?")
    else:
        print("Is your chosen disney character from the show The Owl House?")
        question4=input("Please enter yes or no.")
        if question4 == "yes":
            print("Is your chosen disney character male?")
            question5=input("Please enter yes or no.")
            if question5 =="yes":
                print("You have chosen Hunter.")
                correct=input("Is this correct (yes, no)?")
            else:
                print("You have chosen Luz.")
                correct=input("Is this correct (yes, no)?")
        else:
            print("You have chosen Maleficent.")
            correct=input("Is this correct (yes, no)?")
        
    
