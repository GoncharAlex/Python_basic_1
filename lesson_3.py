'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


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

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''


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


user_data(name='Alex', surname='Gonchar', year=1989, city='Moscow', email='zojevec@mail.ru', phone=12345)

'''
3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
Решение: перевожу введеные числа в список. С помощью функции max нахожу наибольшее число из этого
списка. Присваиваю его в переменную max_number_1 и затем удаляю из списка. Аналогичная операция
для второго наибольшего числа. 
'''


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

'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде 
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_func_pow_first(x, y):
    """
    my_func_pow returns exponentiation of number x on number y by function **
    :param x:positive number (int)
    :param y: negative number (int)
    :return: exponentiation (int)
    """
    return (x ** abs(y))


print(my_func_pow_first(5, -3))


def my_func_pow_second(x, y):
    """
    my_func_pow returns exponentiation of number x on number y by 'while'
    :param x: positive number (int)
    :param y: negative number (int)
    :return: exponentiation (int)
    """
    result = x
    y = abs(y)
    i = 1
    while i < y:
        result = result * x
        i = i + 1
    return result


print(my_func_pow_second(4, -3))

'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к 
уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму 
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

remember_number = 0  # переменная, которая будет записывать в себя сумму введённых чисел
exit_symbol = None  # переменная для выхода из цикла

while exit_symbol != 'q':
    user_numbers = input('Введите строку чисел, разделенных пробелом (для выхода введите "q"): ')
    arguments_for_sum = []
    user_list = user_numbers.split()
    for itm in user_list:
        if itm.isdigit():
            itm = float(itm)
            arguments_for_sum.append(itm)
        elif itm == 'q':
            exit_symbol = 'q'
        else:
            continue
    print(remember_number + sum(arguments_for_sum))
    remember_number = remember_number + sum(arguments_for_sum)

'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
 и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать 
написанную ранее функцию int_func().
Решение: строку с пробелами я разделяю методом split и превращаю в список. 
Циклом for прохожусь по его элементам и заменаю его элемент на элемент с заглавной буквой. 
Добавляю слово в переменную result_string, которую после этого методом join превращаю
снова в строку. 
'''


def int_func(user_string):
    """
    function int_func returns words with big first letter
    :param user_string: str
    :return: str
    """
    result_string = []
    user_string = user_string.split(' ')
    for itm in user_string:
        itm = itm[0].upper() + itm[1:]
        result_string.append(itm)
    result_string = ' '.join(result_string)
    return result_string


print(int_func('my program is working'))
