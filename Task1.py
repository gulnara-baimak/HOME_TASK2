#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Попробовать решить не переводя числа в строку
#Пример: 6782 -> 23   0,56 -> 11

#input() --> для ввода
#list(input()) --> разбить введенное на цифры
#map(int, list(input())) --> каждую цифру привести к целому (у нас ведь изначально текст)
#sum(map(int, list(input()))) --> посчитать сумму цифр
#print(sum(map(int, list(input())))) --> вывести сумму


#print('Введите число: ')
#print(sum(map(int, list(input()))))

#1 ВАРИАНТ 
a = input('Введите число:  ')

def summa(a):                            #функция нахождения суммы чисел в заданном числе
    if float(a) < 0:                            #Проверка на знак перед числом
        a = float(a) * (-1)
    number = 0

    for i in str(a):
        if i != '.':
            number += int(i)
    return number
print(f'Сумма цифр введенного числа равна: {summa(a)}')

#2 ВАРИАНТ (вариант через строку)
num = input('Введите число:  ')
num= str(num)
summa: int = 0
for i in num:
    print (i.isdigit())
    if i.isdigit():
        summa +=int(i)
print(f'Сумма цифр введенного числа равна: {summa}')

# float_num = input('input float number: ')

# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# x =float(0.25 % 0.04)
# print(round((x), 2))

#  if x > 1 or x < -1:
#         while x != 0:                        #Нахождение суммы
#             number = x % 10 + number
#             x = int(x / 10)
#     elif x < 1 and x > -1:
#         while x != '.':
#             number +=  int
#     return number


#x=0,56
#print(sum(map(int,str(x))))


#def s(a):
#  result = 0
 #   while a > 0:
  #      result += a % 10
   #     a //= 10
    #return result
 
#print(s(0,56))


#n = int(input("Введите число:"))
#tot = 0
#while(n > 0):
#    dig = n % 10
#    tot = tot + dig
#    n = n//10
# print("Сумма цифр равна:", tot)