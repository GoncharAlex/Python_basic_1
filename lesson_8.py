'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def first_method(cls, param: str):

        result = []
        for itm in param.split('-'):
            if itm.isdigit():
                itm = int(itm)
                result.append(itm)
        return result


    @staticmethod
    def second_method(param_str: str):

        idx = 0
        result = []
        for itm in param_str.split('-'):
            if itm.isdigit():
                itm = int(itm)
                result.insert(idx, itm)
                idx += 1
            try:
                if 0 < result[1] < 13:
                    return print('Валидация прошла успешно!')
            except Exception:
                continue

date = Date('22-10-1989')
# date = date.first_method('22-10-1989')
print(date.second_method('22-10-1989'))
print(1)


'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию и 
не завершиться с ошибкой.
'''

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    if second_number == 0:
        raise MyException('На ноль делить нельзя!')
except MyException as e:
    print(e)

