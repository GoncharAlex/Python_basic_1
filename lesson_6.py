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

