#chatbox

name=input("What is your name?")
print("Hello " + name)
print("My name is Ami.")

def age():
    age=int(input("How old are you?"))
    print("I am", age, "too.")
age()

def feelings():
    feelings=input("How are you feeling?")
    positivefeelings=["good", "amazing", "happy", "hopeful","joyful"]
    if feelings in positivefeelings:
        print("That is great!")
    else:
        print("Sorry to hear that.")
feelings()

def weather():
    weather=input("What is the weather like?")
    weatherlist1=["sunny", "Sunny", "Hot", "hot"]
    weatherlist2=["cloudy", "Cloudy", "Foggy", "foggy", "cold", "Cold"]
    if weather in weatherlist1:
        print("That is fantastic!")
    elif weather in weatherlist2:
        print("You can still go outside.")
    else:
        print("That isn't good")
weather()

def faveSubject():
    subject=input("What is your favourite subject?")
    languages=["french", "French", "Spanish", "spanish"]
    if "computing" in subject:
        print("I agree this is the best subject.")
    elif subject in languages:
        print("I disagree this is the worst subject.")
    else:
        print("This is an alright subject.")
faveSubject()

def friends():
    print("Are we friends?")
    friends=input("Please say yes, no or maybe.")
    if "yes" in friends:
        print("That makes me happy.")
    elif "no" in friends:
        print("That makes me sad.")
    else:
        print("That confuses me.")
friends()
