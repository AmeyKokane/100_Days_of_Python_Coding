from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# question = Question()

for i in question_data:
    new_question= Question(q_text=i['question'],q_answer=i['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions:
    quiz.next_question()

#print(question_bank[0].text)
print("You have completed the quiz!")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
