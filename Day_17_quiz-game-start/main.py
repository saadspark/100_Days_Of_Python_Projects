from question_model import Question
from quiz_brain import QuizBrain
from data import question_data



question_bank = []
for question in question_data :
    question_text = question['text']
    question_answer = question['answer']
    new_Question = Question(question_text,question_answer)
    question_bank.append(new_Question)



quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question() :
    quiz_brain.new_question()

print("You have completed the quiz")
print(f"Your final score is : {quiz_brain.score}/{quiz_brain.question_number}")