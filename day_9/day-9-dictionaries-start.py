# создание словаря
programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
}
# отобразить значение по ключу
print(programming_dictionary["Bug"])

# присвоить ключу иное значение
programming_dictionary["Function"] = "Other value"
print(programming_dictionary["Function"])

# создать новый item (элемент)
programming_dictionary["New key"] = "New value"
print(programming_dictionary["New key"])

# цикл отображения каждого ключа, затем каждого значения
for key in programming_dictionary:
	print(key)
	print(programming_dictionary[key])


# конспект от чат ГПТ:
# Создание пустого словаря
empty_dict = {}

# Создание словаря с помощью функции dict()
another_dict = dict()

# Добавление новой пары ключ-значение
programming_dictionary["Key"] = "Value"

# Удаление пары ключ-значение по ключу
del programming_dictionary["Key"]
# или
programming_dictionary.pop("Key")

# Удаление последнего элемента:
programming_dictionary.pop()

# Получение значения по ключу с помощью метода get()
value = programming_dictionary.get("Bug")

# Получение значения по ключу с помощью оператора квадратных скобок []
value = programming_dictionary["Bug"]

# Получение всех ключей словаря
keys = programming_dictionary.keys()

# Получение всех значений словаря
values = programming_dictionary.values()

# Получение всех пар ключ-значение в виде кортежей
items = programming_dictionary.items()

# Очистка словаря
programming_dictionary.clear()

# Копирование словаря
copied_dict = programming_dictionary.copy()

# Обновление словаря с использованием другого словаря или итерируемого объекта
new_dict = {"New Key": "New Value"}
programming_dictionary.update(new_dict)

# Проверка наличия ключа в словаре
if "Bug" in programming_dictionary:
    print("Bug is present in the dictionary.")
else:
    print("Bug is not present in the dictionary.")

# Итерация по парам ключ-значение
for key, value in programming_dictionary.items():
    print(key, value)