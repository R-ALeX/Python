# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 1000
b = 'MyCode'
c = True
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
e = input('Введите значение: ')
print('-----------------------------')

#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
from datetime import datetime, date, time

t = int(input('Введите Значение: '))
f = datetime.now()
t1 = time(f.hour, f.minute, t)
print(t1)

print('-----------------------------')

#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = str(input('Введите Значение: '))
summ = int(n) + int(n+n) + int(n+n+n)
print(summ)

print('-----------------------------')

#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите Значение: '))
ls = []
while number > 10:
    ls.append(number % 10)
    number //= 10
r = max(ls)
print(r)
print('-----------------------------')

#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = float(input('Введите доход компании: '))
expense = float(input('Введите расход компании: '))
if income > expense:
    print('Компания доходная')
elif income < expense:
    print('Компания убыточная')
elif income == expense:
    print('С - стабильность')
print('-----------------------------')

#6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

myA = float(input('Резулютат в первый день: '))
myB = float(input('Оезультат, который должен быть: '))
i = 1
print(i, ' день: ', myA),
while myA < myB:
    i += 1
    myA = myA + myA * 0.1
    print(i, ' день: ', myA),
print(i, ' дней тренировок')
