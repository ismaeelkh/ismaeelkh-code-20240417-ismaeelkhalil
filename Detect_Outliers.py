import pandas as pd
import numpy as np

class Detect_Outliers:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    
    def inter_quartiles(self, col : str = '', cutoff_bottom: float = 0.00, cutoff_top: float = 0.00):
        # Method to return quartile
        return self.df[col].quantile(cutoff_bottom), self.df[col].quantile(cutoff_top)
    
    def lower_upper_bound(self, col: str = '', cutoff_bottom: float = 0.00, cutoff_top: float = 0.00, multiplier: str = 0.00):
        # Method to compute lower and upper bounds
        Q1, Q3 = self.inter_quartiles(col, cutoff_bottom, cutoff_top)
        lower_bound = Q1 - (multiplier * (Q3 - Q1))
        upper_bound = Q3 + (multiplier * (Q3 - Q1))

        return lower_bound, upper_bound
    
    def detect_outliers(self, col: str = '', cutoff_bottom: float = 0.00, cutoff_top: float = 0.00, multiplier: str = 0.00):
        # Method to detect outliers
        lower_bound, upper_bound = self.lower_upper_bound(col, cutoff_bottom, cutoff_top, multiplier)
        return self.df[~self.df[col].between(lower_bound, upper_bound)].reset_index(drop = True)
        
    
    def remove_outliers(self, col: str = '', cutoff_bottom: float = 0.00, cutoff_top: float = 0.00, multiplier: str = 0.00):
        # Method to remove outliers
        lower_bound, upper_bound = self.lower_upper_bound(col, cutoff_bottom, cutoff_top, multiplier)
        self.df = self.df[self.df[col].between(lower_bound, upper_bound)].reset_index(drop = True)
        return self.df
    
    
    
    