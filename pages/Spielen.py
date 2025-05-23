import streamlit as st
import game.entity
from game.controller import Controller

ctr = Controller(st=st)

ctr.meta('Spielen', '▶️')
cats = game.entity.Categories()

with st.form("my_form"):
   st.write("Kategorie")
   my_color = st.selectbox('Kategorie', cats.all())
   if st.form_submit_button('ok'):
       ctr.save_success()
       