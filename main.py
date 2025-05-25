# Bootstrapping Quiz application
# AUTHOR Sven Schrodt
# SINCE 2025-05-22

import pyquiz.mock
import pyquiz.app
import pyquiz.entity
import pandas as pd
import random
import html
from t00lZ.scrape import Scrape as Scrape


mock = pyquiz.mock.Mock() 
df = mock.filterable



l = len(df)
rnd = random.randint(0, l-1)
print(f'Länge: {l} Zufallszahl: {rnd}')

question = df.iloc[rnd]
my_quest = pyquiz.entity.Question(question)
print(my_quest.question)
print(my_quest.answers, type(my_quest.answers))