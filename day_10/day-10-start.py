# Output functions - функции с выводом

# Определение функции для форматирования имени и фамилии
def format_name(f_name, l_name):
    # Преобразование первой буквы имени в верхний регистр
    formated_f_name = f_name.capitalize()
    # Преобразование первой буквы фамилии в верхний регистр
    formated_l_name = l_name.capitalize()
    # "Возврат" отформатированного имени и фамилии вместе = ЗАМЕНА ФУНКЦИИ РЕЗУЛЬТАТОМ ЕЁ ВЫПОЛНЕНИЯ
    # return = конец работы функции, даже если результат пустой
    return f"{formated_f_name} {formated_l_name}"

# Вызов функции с передачей имени и фамилии в качестве аргументов и вывод результата
print(format_name("алял", "хУЯМбус"))
