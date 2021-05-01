#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
import itertools
import colorama
from colorama import Fore, Back

colorama.init()

class TrafficLight:
    __colors = ["RED","YELLOW","GREEN"]

    def running(self):
        i = 1
        for light in itertools.cycle(self.__colors):
            if i == 4:
                i = 1;
            if i == 1:
                print(Back.RED + Fore.BLACK + light)
                time.sleep(7)
            elif i == 2:
                print(Back.YELLOW + Fore.BLACK + light)
                time.sleep(2)
            elif i == 3:
                print(Back.GREEN + Fore.BLACK + light)
                time.sleep(7)
            i += 1

traffic = TrafficLight()
traffic.running()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def RoadWeight(self, weight=25, thicknesses=5):
        return print("Result is:", self._lenght * self._width * weight * thicknesses/1000)

fRoad = Road(5000,20)
fRoad.RoadWeight()


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, fName, sName, position, wage, bonus):
        self.fName = fName
        self.sName = sName
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def fullName(self):
        return print("First Name:", self.fName , "Second Name:", self.sName)

    def profit(self):
        return print("Profit is:", sum(self._income.values()))

employer = Position("Pedro", "Gansalez", "Taxi Driver", 15000, 1200)
employer.fullName()
employer.profit()

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False ):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(self.name,"car's gone")

    def stop(self):
        return print(self.name,"car's stop")

    def turn(self, direction):
        return print(self.name,"car's turn on", direction)

    def showSpeed(self):
        return print(self.name,"speed is", self.speed)

class TownCar(Car):
    def showSpeed(self):
        if self.speed > 60:
            return print(self.name,"speed is", self.speed, "exceeding the speed!!!")
        else:
            return print(self.name, "speed is", self.speed)

class WorkCar(Car):
    def showSpeed(self):
        if self.speed > 40:
            return print(self.name,"speed is", self.speed, "exceeding the speed!!!")
        else:
            return print(self.name, "speed is", self.speed)

bmw = TownCar(250, "Black", "BMW")
bmw.go()
bmw.showSpeed()
bmw.turn('Right')

#5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title) -> object:
        self.title = title

    def draw(self):
        return print("I am drawing")

class Pen(Stationery):
    def draw(self):
        return print("I draw", self.title, "it's a  pen!")

class Pencil(Stationery):
    def draw(self):
        return print("I draw", self.title, "it's a percil!")

class Handle(Stationery):
    def draw(self):
        return print("I draw", self.title, "it's a handle!")

pen = Pen("ballpoint pen")
pen.draw()

pencil = Pencil("Red pencil")
pencil.draw()

handle = Handle("Black Handle")
handle.draw()