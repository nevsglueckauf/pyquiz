# Class for mocking data (avoiding consuming online API)
#
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16

import pandas as pd
import json
from typing import Self, Any
#import game.mock 


class Mock:
    """ Mock data for:
            - developing phase
            - testing while development process
            - continuous unit testing (CI/CD pipeline)
    """
    questions:list
    filterable:pd.DataFrame
    mock_file:str = 'data/question.json'  
    curr_fltr:str
    
    def __init__(self):
        tmp = json.load(open(self.mock_file))
    
        self.questions = tmp['results']
        self.filterable = pd.DataFrame(data = self.questions, columns=self.questions[0].keys()) 
       
    def get_question_bool(self):
        return {'type': 'boolean', 'difficulty': 'medium', 'category': 'History', 'question': 'Ottoman Empire was created in 1299.', 'correct_answer': 'True', 'incorrect_answers': ['False']}
    
    def get_question_multiple(self):
        return {'type': 'multiple', 'difficulty': 'medium', 'category': 'Entertainment: Video Games', 'question': 'What is the lowest amount of max health you can have in Team Fortress 2?', 'correct_answer': '70', 'incorrect_answers': ['100', '50', '95']}
    
    def filter_by(self, key:str) -> Self:
        self.curr_fltr = key
        return self
    
    def equals(self, val:str):
        return self.filterable[self.filterable[self.curr_fltr] == val]
        
        #-> pd.DataFrame:
        # return self.filterable[key] 
    
    
    

