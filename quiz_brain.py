class Quizbrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        last_question = len(self.question_list)-1
        return self.question_number <= last_question

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number +=1
        answer = input(f'Q.{self.question_number}:{question_text} True or False ')
        return answer == question_answer
