# Bootstrapping Quiz application
# AUTHOR Sven Schrodt
# SINCE 2025-05-22

import game.mock
import game.app
import game.entity
import pandas 
import random
import html
from t00lZ.scrape import Scrape as Scrape

Scrape.me(23)
exit()
mock = game.mock.Mock()
df = pandas.DataFrame(mock.questions)

df["category"] = df['category'].apply(lambda x: html.unescape(x))

print(df["category"].unique)
#df["question"] = html.unescape(df["question"])
#print(df)

#print('lorem Ipsum'.title())
print(12)

#dta = mock.filter_by('category').equals('History')
my_app = game.app.App()
#print(my_app)
# print((len(mock.questions)))
#questions = game.entity.QuestionList(game.mock.questions)


#print(questions)