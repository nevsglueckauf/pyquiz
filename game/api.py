# trivia python script managing http traffic 
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16

import json
import requests

class Trivia:
    req: requests
    dta: dict
    main_uri:str = ' https://opentdb.com/api.php?amount={}'
    response_code:int
    
    def __init__(self):
        pass
    
    def get_questions_raw(self, number:int=10) -> dict:
        response = requests.get(self.main_uri.format(number))
        self.response_code=  response.status_code
        self.dta = response.json()
        return self.dta['results']