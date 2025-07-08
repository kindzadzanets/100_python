from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for index in range(0, len(question_data)):
    question = Question(question_data[index]["question"], question_data[index]["correct_answer"])
    question_bank.append(question)

# вариант от джеппето:

# question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]

# Это называется list comprehension — "списковое включение", 
# и оно делает ровно то же самое, но в одной строке, понятнее и быстрее.


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.end_quiz()



