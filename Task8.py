#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year,
        self.month = month,
        self.day = day

    @classmethod
    def extract(cls, data):
        data = data.split("-")
        data = list(map(int, data))
        print(f"this is year {data[2]}, this is month {data[1]}, this is day {data[0]}")
        year = data[2]
        month = data[1]
        day = data[0]
        return cls(year, month, day)


    @staticmethod
    def check_date(obj):
        if int(obj.month[0]) > 12 or int(obj.month[0]) < 1:
            print("Wrong month number!!!")
        elif int(obj.year[0]) > 2020 or int(obj.year[0]) <= 1900:
            print("Wrong year number!!!")
        elif int(obj.day) > 30 or int(obj.day) < 1:
            print("Wrong day number!!!")
        else:
            return datetime.date(int(obj.year[0]),int(obj.month[0]),int(obj.day))

mydate = input("insert date type (dd-mm-yyyy):")
mydate = Date.extract(mydate)
mydate = Date.check_date(mydate)
print(mydate)


#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Div:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, num2):
        if num2 == 0:
            self.__num2 = 1
        else:
            self.__num2 = num2


myDiv1 = Div(int(input('Insert 1 number:')), int(input('Insert 2 number:')))
print(myDiv1.num1 / myDiv1.num2)


#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Insert number in list:')
        if value == '!':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('it doesn,t number!', ex)
print(my_list)


#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

#5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

#6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_lists = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Count': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} count {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Enter name ')
            unit_p = int(input(f'Enter price '))
            unit_q = int(input(f'Enter count '))
            unique = {'Model': unit, 'Price': unit_p, 'Count': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current List -\n {self.my_store}')
        except:
            return f'Data insert error'

        q = input(f'For exit - Q.Press <-')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'All WH -\n {self.my_store_full}')
            return f'Exit'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.number_of_lists} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.number_of_lists} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth {self.number_of_lists} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

#7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Amount of num1 and num1')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'multiplication of num1 and num1')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(12, -52)
z_2 = ComplexNumber(34, 42)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)