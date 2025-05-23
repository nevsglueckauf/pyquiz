# Classes representing entities for Trivia DB Game
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
#
# Question - representing single trivia game question
import pandas as pd
import random
import html
import json
from typing import Any, Self, Dict, List, Optional, Sequence, Tuple, Union


class Question:

    # valid indices (keys in this case)
    __idc = [
        "type",
        "difficulty",
        "category",
        "question",
        "correct_answer",
        "incorrect_answers",
        "answers",
    ]
    dta: dict
    given_answer: str
    result: bool

    def __init__(self, dta: dict):
        self.dta = dta
        self.dta["answers"] = self.dta["incorrect_answers"]
        self.dta["answers"].append(self.dta["correct_answer"])
        self.dta["question"] = html.unescape(self.dta["question"])
        self.dta["answers"] = list(map(lambda x: html.unescape(x), self.dta["answers"]))
        random.shuffle(self.dta["answers"])  # get questions in a randomized order
        
    def answer(self, answer: str) -> Self:
        answer = self.__sanitize_answer(answer)
        if answer not in self.dta["answers"]:
            raise ValueError(f"Value {answer} is not a possible answer!")
        self.given_answer = answer
        return self

    def solve(self):
        if self.given_answer is None:
            raise ValueError(f"Not an answer given yet !")
        self.result = self.correct_answer == self.given_answer

    def __getattr__(self, key):
        self.__sanitize_key(key)
        return self.dta[key]

    def __str__(self) -> str:
        my_str = "Cat: " + self.dta['category'] + " [Diff: " + self.dta['difficulty'] + "]"
        my_str += "\n"
        my_str += "Question: " + self.dta["question"]
        my_str += "\n"
        for idx, x in enumerate(self.dta["answers"]):
            my_str += str(idx + 1) + ' ' + str(x)
            my_str += "\n"

        return my_str

    def __sanitize_key(self, key: str):
        if key not in self.__idc:
            raise IndexError(f"Key {key} does not exist")

    def __sanitize_answer(self, input):
        return str(input)


class QuestionList:

    filterable: pd.DataFrame
    curr_fltr: str

    def __init__(self, dta: list):
        self.filterable = pd.DataFrame(data=dta, columns=dta[0].keys())

    def filter_by(self, key: str) -> Self:
        self.curr_fltr = key
        return self

    def equals(self, val: any) -> pd.DataFrame:
        return self.filterable[self.filterable[self.curr_fltr] == val]

class Categories:
    catz:pd.DataFrame # of dict
    cat_fl:str = 'data/category.json'
    
    def __init__(self):
        
        self.catz = pd.DataFrame(json.load(open(self.cat_fl))['trivia_categories'])
        
    def all(self):
        all = ['any']
        return all + list(self.catz['name'])      
        
    def byId(self, cid:int):
        
        #print(self.catz[self.catz['id']==cid])
        return self.catz[self.catz['id']==cid]['name'].iloc[0]
    
    def getId(self, cname:str):
        
        return self.catz[self.catz['name']==cname]['id'].iloc[0]
    
    
