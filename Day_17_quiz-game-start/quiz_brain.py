class QuizBrain : 
       
    def __init__(self,question_list) :
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def still_has_question(self) :
        return self.question_number < len(self.question_list)
    
    def check_answer(self,given_answer,actual_answer) :
        if(actual_answer.lower() == given_answer.lower()) :
            self.score += 1
            print(f'You got it ! || Current score : {self.score}/{self.question_number}')
            
           
        else :
            print(f'That\'s wrong ! Correct Answer is : {actual_answer} || Current score : {self.score}/{self.question_number}')
          

    
    def new_question(self) :
        self.question_number += 1
        given_answer = input(f'Q.{self.question_number } : {self.question_list[self.question_number-1].text}. (True/False) ? ')        
        self.check_answer(given_answer,self.question_list[self.question_number-1].answer) 
        print('\n')  
