#Реализуйте алгоритм перемешивания списка, 
# без использования встроеных методов (особенно SHUFFLE, без него) 
# можно (нужно) использовать библиотеку Random

import random

myList = []
for i in range(10):
    myList.append(random.randint(0, 25))
print('Первоначальный список: ' + str(myList))

for i in range(len(myList)- 1):
    j = random.randint(0, len(myList)- 1)
    myList[i], myList[j] =  myList[j], myList[i]

print('Перемешанный список: ' + str(myList))