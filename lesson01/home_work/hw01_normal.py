# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
print('Введите, пожалуйста, двухзначное число')
n = input()
p = str(n)
m = list(p)

if int(m[0]) == int(m[1]):
    print('Числа равны')
elif int(m[0]) > int(m[1]):
    print('Самая большая цифра числа ', m[0])
else:
    print('Самая большая цифра числа ', m[1])
    
    
    

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

print('введите число a')
a = input()
print('введите число b')
b = input()

def foo():
    a = b
    print(a)

def foo1():
    b = a
    print(b)

print ('Вы ввели ')
foo()
foo1()

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4
