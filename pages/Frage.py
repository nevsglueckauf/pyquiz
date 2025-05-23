import streamlit as st
import game.entity
import game.config
import game.mock
import game.entity
import random
from game.controller import Controller

ctr = Controller(st=st)
ctr.meta("Frage (Prototyp)", "🤸‍♂")
cats = game.entity.Categories()
cfg = game.config.Config()
mock = game.mock.Mock()
st.markdown('## Zufallsauswahl')
df = mock.filterable
l = len(df)
rnd = random.randint(0, l - 1)
question = df.iloc[rnd]
my_quest = game.entity.Question(question)

with st.form("my_question"):
    st.html("<fieldset><legend>" + " | ".join([my_quest.category, my_quest.type, my_quest.difficulty]) + "</legend></fieldset>")
    
    st.write(my_quest.question)
    st.radio("Antworten:", my_quest.answers, index=None)
    st.html(f"""<details>
                    <summary>Cheat!</summary>
                    {my_quest.correct_answer}
                </details>""")
    if st.form_submit_button("ok"):
        ctr.save_success()
