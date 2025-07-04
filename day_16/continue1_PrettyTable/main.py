from prettytable import PrettyTable

table = PrettyTable() #создание объекта "таблица" из класса PrettyTable, импортированного из готового модуля
table.add_column(
    "Страна",
    [
        "Исландия",
        "Дания",
        "Ирландия",
        "Новая Зеландия",
        "Австрия",
        "Сингапур",
        "Португалия",
        "Словения",
        "Япония",
        "Швейцария",
    ],
) # добавление колонки: первая строка - заголовок колонки, далее - список срок в колонке
table.add_column(
    "Столица",
    [
        "Рейкьявик",
        "Копенгаген",
        "Дублин",
        "Веллингтон",
        "Вена",
        "Сингапур",
        "Лиссабон",
        "Любляна",
        "Токио",
        "Берн"
    ],
) # добавление второй колонки

table.align = "l" # изменение атрибута "выравнивание" для всего объекта
table.align["Столица"] = "r" # изменение выравнивания для конкретной колонки по заголовку
print(table)