import streamlit as st
import pyquiz.entity
import pyquiz.config
import pyquiz.mock
import pyquiz.entity
import random
from pyquiz.controller import Controller
import pandas as pd 
import numpy as np
ctr = Controller(st=st)
ctr.meta("Statistiken, Logs, Metriken (Platzhalter)", "📈")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.markdown('Lorem Ipsum blah blubb')
chart_data_2 = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data_2, x="col1", y="col2", color="col3")


