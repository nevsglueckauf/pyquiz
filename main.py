# Bootstrapping Quiz application
# AUTHOR Sven Schrodt
# SINCE 2025-05-22

import game.mock

mock = game.mock.Mock()
dta = mock.filter_by('category').equals('History')
# app = game.app.App()

print((len(mock.questions)))
#questions = game.entity.QuestionList(game.mock.questions)


#print(questions)