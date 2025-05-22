# Bootstrapping Quiz application
# AUTHOR Sven Schrodt
# SINCE 2025-05-22

import game.mock
import game.app
import pandas 

mock = game.mock.Mock()
df = pandas.DataFrame(mock.questions)
catz = df['category'].unique()
catz.sort()

print('\n'.join(list(catz)))

dta = mock.filter_by('category').equals('History')
my_app = game.app.App()
print(my_app)
# print((len(mock.questions)))
#questions = game.entity.QuestionList(game.mock.questions)


#print(questions)