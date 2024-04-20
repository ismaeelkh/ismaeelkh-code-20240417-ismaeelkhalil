import pandas as pd
import numpy as np


class Data_Type:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    

    def check_data_type(self, col: str = '', data_type: str = ''):
        self.col = col
        self.data_type = data_type
        return self.df[col].dtype == self.data_type
    

    def change_data_type(self, new_data_type: str = ''):
        self.new_data_type = new_data_type
        self.df[self.col] = self.df[self.col].astype(self.new_data_type)
        return self.df[self.col].dtype

    
    def change_inf_values(self):
        self.df[self.col] = self.df[self.col].replace([np.inf, -np.inf], np.nan)
        return self.df
    
    def change_date_variables(self):
        # We convert all columns that have 'date' in their header names into datetime64[ns] type
        self.df[self.df.columns[self.df.columns.str.contains('date')]] = self.df[self.df.columns[self.df.columns.str.contains('date')]].astype('datetime64[ns]')
        return self.df
        

