from mock import Mock

t = Trivia()
m = Mock()
game = app.App()
#foo = app.Runner()
#print(str(True),str(False))
#exit(5363)
data  = t.get_questions_raw(2)
print(data[0])   

print(data[1])

exit(666)

#print(data['results'][0])
data = m.get_question_multiple()
#data= m.get_question_bool()
#print(t.response_code)
q1 = Question(data)
q1.answer(100)
game.runner.render(q1)
#print(q1.correct_answer)
#print(type(q1.correct_answer), type(q1.given_answer))
#print(q1.correct_answer == q1.given_answer)

q1.solve()
print(q1.result)

# print(q1.dta['answers'])
#print(type(q1.dta['incorrect_answers']), q1.dta['incorrect_answers'])


mock = Mock() 
df = mock.filterable
print(df[df['type'] == 'boolean'])   #.unique())
no_17 = dict(df.iloc[27])
print(no_17['question'])