from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
right_answers = 0
out_of = 0

for a in question_data:
    question = a['text']
    answer = a['answer']
    new_question_object = Question(question, answer)
    question_bank.append(new_question_object)

test = Quizbrain(question_bank)
while True:
    if test.still_has_questions():
        result = test.next_question()
        if result is True:
            right_answers +=1
    else:
        print(f'Game over!')
        break
    out_of +=1
    print(f'Results {right_answers}/{out_of}')

