numbers=[1, 2, 3, 4, 5]
print(numbers[0],numbers[1],numbers[2])
print("Array is:", numbers)
res=numbers[::-1]
print("Resultant new reversed array:", res)
numbers.append(3)
print(numbers)
from array import *
array_num=numbers("i", [1, 2, 3, 4, 5, 3])
print("Number of occurrences of the number 3 in the array:" + str(array_num.count(3)))
numbers.pop(5)
print(numbers)
