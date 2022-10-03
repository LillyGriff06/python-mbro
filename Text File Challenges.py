#Challenges
data1 = "These are some random symbols: 25hf@$"
data2 = "Here is some more random data: 875dgv#!*"

def write():
    with open("TextFileChallenges.txt", "w") as file:
        file.write("\n" + data1 + "\n")
        file.close()
write()

def append():
    with open("TextFileChallenges.txt", "a") as file:
        file.write("\n" + data2 + "\n")
        file.close()
append()

def linePrepender(filename, line):
    with open(filename, "r+") as file:
        content = file.read()
        file.seek(0, 0)
        file.write(line.rstrip("\r\w") + "\n" + content)
linePrepender(filename="TextFileChallenges.txt", line="text")
