# 🚨 Don't change the code below 👇
# запросить значения роста через пробел и преобразовать в список командой split()
student_heights = input("Input a list of student heights:\n").split()
# преобразовать элементы списка из строки в число
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# отобразить список
print(student_heights)
# 🚨 Don't change the code above 👆

# ЗАДАЧА: Необходимо вычислить средний рост ученика, опираясь на данные введённые пользователем

# оптимальный путь: разделить сумму ростов студентов на обшее количество элементов списка(количество студентов)
# average = sum(student_heights) // len(student_heights)
# print(average)


# путь с использованием циклов:

# задал переменные для фактических len() & sum()
length_of_list = 0
total_height = 0
# оформил цикл для списка роста студентов
for cycle in student_heights:
  # для посчёта кол-ва элементов в списке: к каждому предыдущему значению length_of_list прибавляется 1, столько раз - сколько есть элементов в списке.(потому-что это цикл)
  length_of_list +=1
  # в цикле, переменная cycle присваивается каждому элементу списка по-очереди, поэтому к каждому предыдущему значению total_height я прибавляю следующее в очереди значение cycle
  total_height +=cycle
# вичислить средний рост студента: сумму ростов в списке разделить(огруглив до целого) на количество элементов(студентов) в списке списка. И отобразить.
print(round(total_height / length_of_list))


# хорошая практика: называть списки множественным значением, например: students_heights, потому-что при создании циклов можно использовать части названия списка, но уже в единственном числе, например:
# for student in student_heights
#   или
# for height in student_heights


# # тренеровка:
# heights_len = 0
# for pozitsia in student_heights:
#   heights_len +=1
# print(heights_len)
#
# heights_sum = 0
# for student_height in student_heights:
#   heights_sum = student_height + heights_sum
# print(heights_sum)
#
# average = round(heights_sum / heights_len)
# print(average)