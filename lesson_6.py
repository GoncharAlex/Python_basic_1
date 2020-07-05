'''
1. Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами
должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''


import time

class TrafficLight:

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        print(self.__color[0])
        time.sleep(5)
        print(self.__color[1])
        time.sleep(3)
        print(self.__color[2])


a = TrafficLight()
print(a.running())


'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). Значения данных атрибутов должны 
передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего 
дорожного полотна. Использовать формулу: длина * ширина * масса асфальта 
для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road(self, weight, length):
        result = weight * self._length * self._width * length
        result_tonn = int(result / 1000)
        return f'Масса асфальта будет составлять {result_tonn} тонн'

road_param = Road(20, 5000)
print(road_param.weight_road(25, 5))



'''
3. Реализовать базовый класс Worker (работник), в котором 
определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и 
ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс 
Position (должность) на базе класса Worker. В классе Position 
реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). Проверить работу 
примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Full name of the worker: {self.name}, {self.surname}')

    def get_total_income(self):
        print(f'Total income is: {self._income["wage"]} and bonus {self._income["bonus"]}')


worker_bob = Position('bob', 'ivanov', 'manager', 100000, 50)
print(worker_bob.get_full_name())
print(worker_bob.get_total_income())

worker_alex = Position('alex', 'petrov', 'lawyer', 500, 10)

print(worker_alex.get_full_name())
print(worker_alex.get_total_income())
print(worker_bob.name)
print(worker_alex.surname)


'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие 
атрибуты: speed, color, name, is_police (булево). А также методы: 
go, stop, turn(direction), которые должны сообщать, что машина поехала, 
остановилась, повернула (куда). Опишите несколько дочерних классов: 
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод 
show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Выполните вызов 
методов и также покажите результат.
'''

import random

class Car:

    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is going!')

    def stop(self):
        print('Car is stoped!')

    def turn(self):
        direction = ['right', 'left']
        print(random.choice(direction))

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    pass


first_car = Car(50, 'green', 'audi')
print(first_car.name, first_car.color)
first_car.go()
first_car.show_speed()
first_car.stop()


second_car = TownCar(70, 'yellow', 'mercedes')
print(first_car.name, first_car.color)
second_car.go()
second_car.show_speed()
second_car.stop()

third_car = PoliceCar(100, 'black', 'ford', True)
print(third_car.name, third_car.color, third_car.is_police)
third_car.go()
third_car.show_speed()
third_car.stop()

