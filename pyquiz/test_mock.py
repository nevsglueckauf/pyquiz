# Main python script running app 
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
from trivia import Trivia
from entity import Question
from mock import Mock
import app 

mock = Mock()

dta = mock.filter_by('category').equals('History')


print(dta)