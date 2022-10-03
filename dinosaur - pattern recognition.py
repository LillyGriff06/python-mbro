correct="no"
print("Welcome to my dinosaur guesser game.")
print("Please choose one of the following dinosaurs: T-rex, Triceratops, Pterodactyl, Stegosaurus, Velociraptor or Diplodocus")
while correct != "yes":
    print("Does your dinosaur have more than two legs?")
    q1=input("Please enter yes or no.")
    if q1 == "yes":
        print("Does your dinosaur have back plates?")
        q2=input("Please enter yes or no.")
        if q2 == "yes":
            print("You have chosen a stegosaurus.")
            correct=input("Is this correct?")
        else:
            print("Does your dinosaur have horns?")
            q3=input("Please enter yes or no.")
            if q3 =="yes":
                print("You have chosen a triceratops.")
                correct=input("Is this correct?")
            else:
                print("You have chosen a diplodocus.")
                correct=input("Is this correct?")
    else:
        print("Does your dinosaur fly?")
        q4=input("Please enter yes or no")
        if q4 == "yes":
            print("You have chosen a pterodactyl.")
            correct=input("Is this correct?")
        else:
            print("Is you dinosaur considered a small dinosaur?")
            q5=input("Please enter yes or no")
            if q5 == "yes":
                print("You have chosen a velociraptor.")
                correct=input("Is this correct?")
            else:
                print("You have chosen a T-rex.")
                correct=input("Is this correct?")
print("Thank you for playing my game.")
