# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores:\n").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
#  # ЗАДАЧА: необходимо вычислить наивысший бал из списка балов учеников

# # оптимальный путь:
# # print(max(student_scores))


# # решение при помощи цикла:
# # задать переменную "высший бал"
# highest_score = 0
# # цикл позволит повторить одни и те же заданные в его условии действия с каждым элементом списка, поочерёдно присваивая значения элементов одной и той же переменной. (одинаковые действия с разными значениями, короч)
# for score in student_scores:
#     # если на данном шаге, значение присвоенное переменной score БОЛЬШЕ значения highest_score, то заменить текущее значение highest_score на значение, находящееся на данном шаге, в переменной score. Если нет, оставить значение highest_score прежним.
#     if score > highest_score:
#         highest_score = score
# # отобразится последнее значение highest_score, присвоенное в результате удовлетворения условия из цикла.
# print(f"The highest score is {highest_score} !!!")



# # # тренеровка
# #
# # highest_score = 0
# # for score in student_scores:
# #     if score > highest_score:
# #       highest_score = score
# # print(f"the highest score is: {highest_score}")




scores_string = input("Enter a scores, separated by ' ' symbol:\n")
# для преобразования строки в список
score_list = scores_string.split() 
# для преобразования строк в списке в числа
for n in range(0, len(score_list)):
    score_list[n] = int(score_list[n])

print(score_list)

# highest = max(score_list) - ГОТОВАЯ ФУНКЦИЯ
# print(highest)
# вычисление наивысшего значения списка при помощи петли
highest = 0
for score in score_list:
    if score > highest:
        highest = score
  
print(highest)


