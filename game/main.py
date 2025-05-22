# Main python script running app 
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
from trivia import Trivia
from entity import Question, QuestionList
from mock import Mock
import app 
import html
#from app import App

mock = Mock()
list = QuestionList(mock.questions)
for item in mock.questions:
    print(html.unescape(item['question']))





exit(33)
dta = list.filter_by('difficulty').equals('hard')
#.filterable.head(27)
#print(dta)
#
#filter_by('type').equals('boolean')
#print(dta)
single_q = Question(dta.loc[19])
print(single_q)
