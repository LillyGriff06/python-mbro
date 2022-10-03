import random
def randomness():
    n=random
    n=random.randint(0,100)
    print(n)
randomness()

def capital_indexes(a):
    b=[]
    for x in a:
        if x.upper() == True:
            b=b.append(a.index(x))
        else: b=b
    print(b)
capital_indexes(a=["A","b","c","d","E","F","g"])

def mid(string):
    enum=list(enumerate(string))
    lastnum=enum[-1][0]+1
    if lastnum % 2 == 0:
        print("")
    else:
        middle=int((len(enum)/2))
        x=enum[middle][1]
        print(x)
mid(string="abcdefg")
