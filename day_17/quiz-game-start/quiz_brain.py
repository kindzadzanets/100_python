class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("Thats right!")
        else:
            print("That's wrong!")
        print(f"The coorect answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n" * 2)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").capitalize()
        self.check_answer(answer, current_question.answer)
        return answer
    
    def end_quiz(self):
        print("Quiz completed!")
        print(f"Your final score is {self.score}/{self.question_number}")



        # с комментариями от джепетто


#         # Определение класса QuizBrain — логика для управления прохождением викторины
# class QuizBrain:

#     # Метод __init__ — конструктор, вызывается при создании нового объекта QuizBrain
#     def __init__(self, questions_list):
#         self.questions_list = questions_list  # список всех вопросов (объекты класса Question)
#         self.question_number = 0              # индекс текущего вопроса (счётчик)
#         self.score = 0                        # количество правильных ответов (счёт)

#     # Метод для проверки ответа пользователя
#     def check_answer(self, answer, correct_answer):
#         if answer.lower() == correct_answer.lower():  # сравнение ответов без учёта регистра
#             self.score += 1                           # увеличиваем счёт, если ответ верный
#             print("That's right!")                    # сообщение об успехе
#         else:
#             print("That's wrong!")                    # сообщение об ошибке
#         print(f"The correct answer is {correct_answer}")                      # вывод правильного ответа
#         print(f"Your current score is {self.score}/{self.question_number}.")  # вывод текущего счёта
#         print("\n" * 2)  # вывод двух пустых строк для читаемости

#     # Метод, который проверяет, остались ли ещё вопросы в списке
#     def still_has_questions(self):
#         return self.question_number < len(self.questions_list)
#         # возвращает True, если индекс текущего вопроса меньше количества вопросов

#     # Метод для вывода следующего вопроса и получения ответа пользователя
#     def next_question(self):
#         current_question = self.questions_list[self.question_number]
#         # берём объект текущего вопроса по номеру
#         self.question_number += 1
#         # увеличиваем счётчик вопросов на 1
#         answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").capitalize()
#         # просим пользователя ввести ответ и делаем первую букву заглавной для удобства сравнения
#         self.check_answer(answer, current_question.answer)
#         # передаём ответ пользователя и правильный ответ в метод проверки
#         return answer
#         # возвращаем ответ (хотя этот return не обязателен, если не используется дальше)

#     # Метод, который вызывается в конце викторины
#     def end_quiz(self):
#         print("Quiz completed!")  # сообщение о завершении викторины
#         print(f"Your final score is {self.score}/{self.question_number}")  # финальный результат




            
   

