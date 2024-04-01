student_scores = {
	"Harry": 81,
	"Ron": 78,
	"Hermione": 99,
	"Draco": 74,
	"Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
# student_grades["Harry"] = "Exceeds Expectations"
# student_grades["Ron"] = "Acceptable"
# student_grades["Hermione"] = "Outstanding"
# student_grades["Draco"] = "Acceptable"
# student_grades["Neville"] = "Fail"

# мой вариант:
for student in student_scores:
	# student_grades[key]
	if student_scores[student] in range(91, 101):
		student_grades[student] = "Outstanding"
	elif student_scores[student] in range(81, 91):
		student_grades[student] = "Exceeds Expectations"
	elif student_scores[student] in range(71, 81):
		student_grades[student] = "Acceptable"
	else:
		student_grades[student] = "Fail"

# изящный вариант:
# Итерация по словарю student_scores, где ключ - имя студента, а значение - его оценка
for student in student_scores:
    score = student_scores[student]  # Получаем оценку студента из словаря student_scores
    # Определение грейда на основе полученной оценки студента
    if score > 90:
        student_grades[student] = "Outstanding"  # Присваиваем студенту грейд "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"  # Присваиваем студенту грейд "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"  # Присваиваем студенту грейд "Acceptable"
    else:
        student_grades[student] = "Fail"  # Присваиваем студенту грейд "Fail"

# Вывод словаря student_grades, содержащего имена студентов и их грейды
print(student_grades)
