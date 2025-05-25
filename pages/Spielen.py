import streamlit as st
import pyquiz.entity
from pyquiz.controller import Controller

ctr = Controller(st=st)

ctr.meta('Spielen', '▶️')
cats = pyquiz.entity.Categories()

with st.form("my_form"):
   st.write("Kategorie")
   my_color = st.selectbox('Kategorie', cats.all())
   if st.form_submit_button('ok'):
       ctr.save_success()
       