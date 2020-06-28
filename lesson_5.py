'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

while True:
    user_input = input('Введите стркоу для файла (для выхода нажмите enter): ')
    if user_input == '':
        break
    user_file = open('user_file.txt', 'a', encoding='UTF-8')
    user_file.write(user_input + '\n')

user_file.close()


'''
2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
'''

lines_count = 0 # переменная для подсчета количества строк
words_count = 0 # переменная для подсчета количества слов

test_file = open('test_file.txt', 'r') # данный файл создал вручную в той же папке,
# что и находится программа. Добавил все файлы с расширением txt в .gitignore, 
# поэтому в коммиты и пуш на ветку эти текстовые файлы не попадут. 
for line in test_file:
    lines_count += 1
print(f'Количество строк в файле: {lines_count}!')

test_file.seek(0) # перевожу курсор в начало файла после метода read().
content = test_file.read()
content = content.split()
for itm in content:
    words_count += 1
print(f'Количество слов в файле: {words_count}')
test_file.close()


'''
3. Создать текстовый файл (не программно), построчно записать фамилии
 сотрудников и величину их окладов. Определить, кто из сотрудников 
 имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
 Выполнить подсчет средней величины дохода сотрудников.
'''

poor_workers = {} # переменная (словарь) для сохранения "бедных" сотрудников
workers_salary = []

workers_file = open('workers.txt')
for line in workers_file:
    worker, pay = line.split()
    pay = float(pay)
    if pay < 20000:
        poor_workers[worker] = pay
    else:
        continue
for key in poor_workers.keys():
    print('Бедные сотрудники: ' + key)

workers_file.seek(0)
for line in workers_file:
    worker, pay = line.split()
    pay = float(pay)
    workers_salary.append(pay)

print('Средняя зарплата сотрудников: ', sum(workers_salary) / len(workers_salary) - 1)


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''

translate_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
test_file_2 = open('test_file_2.txt')
for line in test_file_2:
    new_list = line.split()
    new_list[0] = translate_dictionary[new_list[0]]
    new_test_file_2 = open('new_test_file_2.txt', 'a')
    result = ' '.join(new_list)
    new_test_file_2.write(result + '\n')
test_file_2.close()
new_test_file_2.close()


'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и 
выводить ее на экран.
'''

file_with_numbers = open('file_with_numbers.txt', 'w')
file_with_numbers.write('5 10 15 20 25 30 35 40 45 50')
file_with_numbers.close()

with open('file_with_numbers.txt') as file_with_numbers:
    list_numbers = file_with_numbers.read().split(' ')
    result_list_numbers = []
    for itm in list_numbers:
        itm = float(itm)
        result_list_numbers.append(itm)

print(sum(result_list_numbers))


'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических и лабораторных 
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
не обязательно были все типы занятий. Сформировать словарь, содержащий 
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

lessons_dictionary = {}

lessons_file = open('lessons.txt')
content_lessons = lessons_file.read().split('\n')
for line in content_lessons:
    line = line.split(' ')
    key = line[0][:-1]
    value = line[1:]
    lessons_dictionary[key] = value

print(lessons_dictionary)

result = {}
for key, value in lessons_dictionary.items():
    result[key] = sum(int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit())

print(result)



