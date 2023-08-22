# импортировать модуль random
import random

# запросить данные и сохранить в переменную. Атрибут .title() переводит первую букву каждого слова в строке в верхний регистр (с Заглавной буквы)
names_string = input("Write all names separated with comma+space (, ):\n").title()

# преобразовать данные в список, деля на элементы по признаку, указанного в () символ(а/ов)
names_list = names_string.split(", ")
# print(names_list)
# print(len(names_list))

# расчитать длинну списка (кол-во элементов) и сохранить полученное значение в переменную
names_list_length = len(names_list)
# print(type(names_list_length))
# print(names_list_length)

# проверка путём предсказуемости "случайного значения"
# seed = int(input("We need a SEED:\n"))
# random.seed(seed)

# случайным образом определить позицию элемента в списке, путём выбора случайного числа в диапазоне (от 0 до (длинна списка - 1)) . Длина списка len() расчитывается от 1, а нумерация элементов с 0.
person_position = random.randint(0, (names_list_length - 1))
# print(person_position)

rich_person = names_list[person_position]
# print(rich_person)

print(f"So, {rich_person} is going to buy the meal today!")