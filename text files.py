data1 = "Hello, this is just some data."
data2 = "Have some more data."
def write():
    with open("data.txt", "w") as file:
        file.write(data1 + "\n")
        file.close()
write()

def append():
    with open("data.txt", "a") as file:
        file.write(data2 + "\n")
        file.close()
append()

def read():
    with open("data.txt", "r") as file:
        file.close()
read()


        
