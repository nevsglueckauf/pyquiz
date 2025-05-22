
# Classes for simpler DF management
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-22
import pandas as pd
from typing import Self

class DFManager:
    
    df:pd.DataFrame # currrent dta
    fltrd:any  # resulting data from filter 
    col_fltr:str # current column for filter actions
    
    def __init__(self, df:pd.DataFrame):
        """ Initializer for DF Manager

        Args:
            df (pd.DataFrame): _description_
        """
        self.df = df
        
    def filter_by(self, key:str) -> Self:
        self.curr_fltr = key
        return self
    
    def equals(self, val:str):
        return self.filterable[self.filterable[self.curr_fltr] == val]
        
    
        