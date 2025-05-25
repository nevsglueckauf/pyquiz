import streamlit as st
import pyquiz.entity
import pyquiz.config
from pyquiz.controller import Controller

ctr = Controller(st=st)

ctr.meta("Spiel konfigurieren", "🎬")
cats = pyquiz.entity.Categories()
cfg = pyquiz.config.Config()

with st.form("my_form"):
    my_amount = st.slider(
        "Anzahl Fragen",
        min_value=cfg.min_amount,
        max_value=cfg.max_amount,
        value=cfg.dft_amount,
    )
    my_cat = st.selectbox("Kategorie", cats.all())
    my_diff = st.selectbox("Schwierigkeitsgrad", cfg.diff)

    if st.form_submit_button("ok"):
        st.write(my_cat, my_diff, my_amount)
        ctr.save_success()
