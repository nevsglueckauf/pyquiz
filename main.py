# Bootstrapping Quiz application
# AUTHOR Sven Schrodt
# SINCE 2025-05-22

import game.mock
import game.app

mock = game.mock.Mock()
dta = mock.filter_by('category').equals('History')
my_app = game.app.App()
print(my_app)
# print((len(mock.questions)))
#questions = game.entity.QuestionList(game.mock.questions)


#print(questions)