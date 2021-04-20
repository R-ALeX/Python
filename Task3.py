#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num1, num2):
    res = num1/num2
    print('Our result is :',res)

try:
    number1 = int(input('Insert number1: '))
    number2 = int(input('Insert number2: '))
    division(number1,number2)
except:
    print('Error!')

print('------------------------------------------')

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def person(fname, sname, BD, city, email, phoneNumber):
    print(f'First name is : {fname}. Second name is : {sname}. Date of birth : {BD}. City of residents : {city}. Email : {email}. Phone number : {phoneNumber} ')


get1Name = input('Insert first name: ')
get2Name = input('Insert second name: ')
getBirthDate = input('insert date of birth: ')
getCity = input('insert city: ')
getEmail = input('insert email: ')
getPhNumber = input('insert phone number: ')
person(fname=get1Name, sname=get2Name, BD=getBirthDate, city=getCity, email=getEmail, phoneNumber=getPhNumber)

print('------------------------------------------')

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func_1(a,b,c):
    list = []
    list.append(a + b)
    list.append(a + c)
    list.append(c + b)
    return max(list)

try:
    a = int(input('Insert 1 number: '))
    b = int(input('Insert 2 number: '))
    c = int(input('Insert 3 number: '))
    result = my_func_1(a,b,c)
    print(result)
except:
    print('Error')

print('------------------------------------------')


#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

#Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    result = x**y;
    return result

def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result * 1/x
    return result

try:
    a = int(input('Insert positive number: '))
    b = int(input('insert negative number: '))
    if b >= 0:
        print('Error!')
    else:
        res = my_func(a, b)
        res2 = my_func2(a, b)
        print(res)
        print(res2)
except:
    print('Error!')

print('------------------------------------------')


#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


row = input('Insert numbers ')
try:
    summ = 0
    while row != '@':
        for number in map(int,row.split(' ')):
            summ += number
        print(summ)
        row = input('Insert numbers ')
except:
    print('Error!')

print('------------------------------------------')


#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#   но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

#Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(insertText):
    insertText = insertText.split()
    newRow = ''
    for word in insertText:
        for i in range(len(word)):
            if i == 0:
                a = word[i].upper()
            else:
                a = a + word[i]
        newRow += ' ' + a
    return newRow.lstrip()

text = input('Insert text: ')
print(int_func(text))