def dictionaryZip():
    keys = ["Ten", "Twenty", "Thirty"]
    values = [10, 20, 30]
    myDict= dict(zip(keys, values))
    print(myDict)
dictionaryZip()

def printingValues():
    sampleDict = {
        "class" : {
            "student" : {
                "name" : "Mike",
                "marks" : {
                    "physics" : 70,
                    "history" : 80
                    }
                }
            }
        }
    print(sampleDict["class"]["student"]["marks"]["history"])
printingValues()

def deleting():
    sampleDict = {
        "name" : "Kelly",
        "age" : 25,
        "salary" : 8000,
        "city" : "New York"
        }
    keysToRemove = ["name", "salary"]
    for k in keysToRemove:
        sampleDict.pop(k)
    print(sampleDict)
deleting()

def renaming():
    sampleDict = {
        "name" : "Kelly",
        "age" : 25,
        "salary" : 8000,
        "city" : "New York"
        }
    sampleDict["location"] = sampleDict.pop("city")
    print(sampleDict)
renaming()

    

    

      
