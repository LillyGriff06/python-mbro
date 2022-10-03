#Divisible by 3

def div_3(number):
    if number%3==0:
        print("true")
    else:
        print("false")
div_3(6)
div_3(5)

#Min-maxing

def largest_difference(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            largest=num1
            if num2>num3:
                smallest=num3
            else:
                smallest=num2
        elif num1 == num3:
            largest=num1
            smallest=num2
        else:
            largest=num3
            smallest=num2
    elif num1 == num2:
        if num1 == num3:
            largest=num1
            smallest=num1
        elif num3 > num1:
            largest=num3
            smallest=num1
        else:
            largest=num1
            smallest=num3
    else:
        if num2 > num3:
            largest=num2
            if num1 > num3:
                smallest=num3
            else:
                smallest=num1
        elif num2 == num3:
            largest=num2
            smallest=num1
        else:
            largest=num3
            smallest=num1
    print(largest - smallest)
largest_difference(num1=2,num2=3,num3=4)
largest_difference(num1=33,num2=33,num3=15)

#Type check

def only_ints(a,b):
    if type(a) == int and type(b) == int:
        print(True)
    else:
        print(False)
only_ints(a=5,b="five")
only_ints(a=7,b=2)

#Counting syllables

def count(word):
    new_word = word
    count_syllables = new_word.split("-")
    print(len(count_syllables))
count(word="ho-tel")
count(word="cat")
count(word="met-a-phor")
count(word="ter-min-a-tor")

#Online status

def online_count(PeopleDictionary):
    for person in PeopleDictionary.items():
        if person[1] == "online":
            count=person.count("online")
            print(count)
statuses={
    "Alice":"online",
    "Bob":"offline",
    "Eve":"online",
    }
online_count(PeopleDictionary=statuses)

#Double letters

def double_letters(word):
    for z in range (len(word)):
        if word[z]==word[z-1]:
            print(True)
        else:
            print(False)
double_letters(word="hello")

#Anagrams

def test_anagrams(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    print(len(str1), len(str2))
    count=0
    if(len(str1))!= (len(str2)):
        print(False)
    else:
        for c in range(0, len(str1)):
            for d in range(0, len(str2)):
                if(str1[c] == str2[d]):
                    count += 1
        if(count == len(str1)):
            print(True)
        else:
            print(False)
test_anagrams(str1="typhoon", str2="opython")

#Flatten a list

def flatten(out_list):
    new_list=[]
    for in_list in out_list:
        for item in in_list:
            new_list.append(item)
    print(new_list)
flatten(out_list=[[1, 2], [3, 4], [5, 6], [7, 8]])


