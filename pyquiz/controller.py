import streamlit  # type: ignore
import pandas as pd
import pyquiz.entity
import pyquiz.config



class Controller:
    """ Controller for page content
    """
    def __init__(self, st: streamlit):
        self.st = st

    def meta(self, title: str = "", icon: str = ""):
        self.st.set_page_config(page_title=title, page_icon=icon)
        self.st.markdown("## " + title)
        self.st.markdown(icon)

    def save_success(self, msg="Daten gespeichert 💾"):
        self.st.write(msg)
        self.st.sidebar.success(msg)


class ViewHelper:
    """ Helper for HTML Views (form elements etc.)
    """
    def __init__(self, st:streamlit):
        self.cats = pyquiz.entity.Categories()
        self.cfg = pyquiz.config.Config()
        self.st = st

    def cats(self):
        return self.st.selectbox("Kategorie", self.cats.all())
        
    def amount(self):
        return self.st.slider(
            "Anzahl Fragen",
            min_value=self.cfg.min_amount,
            max_value=self.cfg.max_amount,
            value=self.cfg.dft_amount,
        )
        
        
    def diff(self):
        return self.st.selectbox("Schwierigkeitsgrad", self.cfg.diff)
