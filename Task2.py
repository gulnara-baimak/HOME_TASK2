#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4) - факториал

n = int(input('Введите число N:'))
f = 1
fact = []
for i in range(1, n+1):
    f = i * f
    fact.append(f)
    print(fact)
  

    