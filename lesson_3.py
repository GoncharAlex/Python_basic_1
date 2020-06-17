'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_division(first_number, second_number):
    """
    My function which division numbers.
    :param first_number: int or float
    :param second_number: int or float
    :return: int or float
    """
    try:
        result = first_number / second_number
        print(result)
    except:
        ZeroDivisionError
        print('На ноль делить нельзя!')

user_choice = None
while user_choice != 'нет':
    user_first_number = int(input('Введите первое число: '))
    user_second_number = int(input('Введите второе число: '))
    my_division(user_first_number, user_second_number)
    user_choice = input('Хотите продолжить (да/нет)? ')
    user_choice.lower()
''' # задание № 1

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year, city, email, phone):
    """
    user_data function prints information about user.
    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: information about user in one line.
    """
    print(f'Человека зовут {name}, фамилия {surname}, он {year} года рождения, живёт в {city}, контакты: {email}, {phone}')

user_data(name='Alex', surname='Goncharov', year=1989, city='Moscow', email='zojevec@mail.ru', phone=12345)
''' # задание № 2

'''
3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
Решение: перевожу введеные числа в список. С помощью функции max нахожу наибольшее число из этого
списка. Присваиваю его в переменную max_number_1 и затем удаляю из списка. Аналогичная операция
для второго наибольшего числа. 

def my_func(first_number, second_number, third_number):
    """
    my_func returns addition of two max elements
    :param first_number: int or float
    :param second_number: int or float
    :param third_number: int or float
    :return: int or float
    """
    numbers = [first_number, second_number, third_number]
    max_number_1 = max(numbers)
    numbers.remove(max_number_1)
    max_number_2 = max(numbers)
    result = max_number_1 + max_number_2
    return result

print(my_func(100, 0, 15))
''' # задание № 3

'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде 
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_pow_first(x, y):
    """
    my_func_pow returns exponentiation of number x on number y by function **
    :param x:
    :param y:
    :return: exponentiation
    """
    return (x ** abs(y))

# print(my_func_pow_first(2, -2)) проверочный print

def my_func_pow_second(x, y):
    """
    my_func_pow returns exponentiation of number x on number y by 'while'
    :param x:
    :param y:
    :return:
    """
    result = x
    y = abs(y)
    i = 1
    while i < y:
        result = result * x
        i = i + 1
    return result

# print(my_func_pow_second(4, -3)) проверочный принт
''' # задание № 4


'''while True:
    positive_number = input('Введите действительное положительное число: ')
    if positive_number < 0 and positive_number != int:
        print('Неверный ввод данных!')
    else:
        break

print(positive_number)''' # ввод пользователя для 4-го задания (не доделанный)
