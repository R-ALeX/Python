#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. .
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

myList = ['twenty-one', 21, hex(21), bin(21), 21.21]
print(myList)
#---------
def check_type(flag):      # Function which return value if type was the same with parametr
    if flag == 'str':
        text = input('Insert text: ')
        try:
            text = float(text)
            print('It s a number!')
        except:
            return text
    elif flag == 'num':
        text = input('Insert number: ')
        try:
            text = float(text)
            return text
        except:
            print('It s a text!')

myList1 = []
p = int(input('Count elements in list: '))
i = 1
while i <= p:       # User input numbers of elements of list. We can add in list text, number, text, number...
    if i % 2 == 0:
        MyType = 'num'
    else:
        MyType = 'str'
    text = check_type(MyType)
    myList1.append(text)
    i += 1
print(myList1)
print('-------------------------------------------')

#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

myList2 = []
p = int(input('Count elements in list: '))
i = 1
while i <= p:
    text = input('Insert value: ')
    myList2.append(text)
    i += 1

i = 0
countElements = len(myList2)
for element in myList2:
    try:
        if i % 2 == 0:
            X = myList2[i]
            myList2[i] = myList2[i + 1]
            myList2[i + 1] = X
    except:
        myList2[i] = X
    i += 1
print(myList2)
print('-------------------------------------------')

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

myList3 = []
p = int(input('Count elements in list : '))
i = 1
while i <= p:
    text = int(input('Insert value between 1 to 12: '))
    if text <= 12 and text > 0:
        myList3.append(text)
    i += 1
print(myList3)

d = {'winter': [], 'spring': [], 'summer': [], 'autumn':[]}

for elements in myList3:
    if elements <= 2 or elements == 12:
        d['winter'].append(elements)
    elif elements > 2 and elements <= 5:
        d['spring'].append(elements)
    elif elements > 5 and elements <= 8:
        d['summer'].append(elements)
    elif elements > 8 and elements <= 11:
        d['autumn'].append(elements)
print(d)
print('-------------------------------------------')

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

phraze = input('Insert text : ')
phraze = phraze.split(' ')
i = 1
for word in phraze:
    print(i,':', word[:10])
    i += 1
print('-------------------------------------------')

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]

my_list = [7, 5, 3, 3, 2]

try:
    new = int(input('Insert number: '))
    my_list.append(new)
    my_list = sorted(my_list, reverse=True)
    print(my_list)
except:
    print('Wrong number!')
print('-------------------------------------------')

#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:

#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]

#Необходимо собрать аналитику о товарах.
#Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:

#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

myList4 = []
tup = ()
p = int(input('Count elements in list : '))
i = 1
while i <= p:
    product = input('Insert name of product: ')
    price = input('Insert price of product: ')
    count = input('Insert count of product: ')
    measure = input('Insert measure of product: ')
    d = {"название": product, "цена": price, "количество": count, "ед": measure}
    tup = (i, d)
    myList4.append(tup)
    i += 1
print(myList4)

analyt = {"название": [], "цена": [], "количество": [], "ед": []}

for number in range(len(myList4)):
    analyt["название"].append(myList4[number][1]["название"])
    analyt["цена"].append(myList4[number][1]["цена"])
    analyt["количество"].append(myList4[number][1]["количество"])
    analyt["ед"].append(myList4[number][1]["ед"])

print(analyt)
print('-------------------------------------------')






















