class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.score = 0
        self.question_number = 0


    def playing(self):
        '''Determines if there are any remaining questions to answer. If so, continue on.'''
        return self.question_number < len(self.question_list)


    def next_question(self):
        '''Cycles through available questions and keeps tally of the current question_number.'''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?\n ~ ')
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        '''Determins if the answer is correct and reports findings. Parameters: user_answer, correct_answer'''
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That is incorrect.')
            print(f'The correct answer was: {correct_answer}')
            
        print(F'Your current score is {self.score}/{self.question_number}\n')