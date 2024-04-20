import pandas as pd

class Missing_Values:
    def __init__(self, df):
        self.df = df


    def display_missing_values(self):
        return self.df.isna().sum()
    
    def drop_null_values(self, col: str = ''):
        # Method to drop null values based on chosen column
        self.df = self.df[~self.df[col].isna()].reset_index(drop = True)
        return self.df
    
    def fill_mean(self, col: str = ''):
        # Method to fill null values with mean of a chosen column 
        avg = self.df[~self.df[col].isna()][col].mean()
        self.df[col] = self.df[col].fillna(avg)
        return self.df

    def fill_median(self, col: str = ''):
        # Method to fill null values with median of a chosen column 
        med = self.df[~self.df[col].isna()][col].median()
        self.df[col] = self.df[col].fillna(med)
        return self.df
    

    def fill_none(self, col : str = ''):
        # Method to fill null values with none
        self.df[col] = self.df[col].fillna("none")
        return self.df
    
    def fill_zero(self, col : str = ''):
        # This method fills nulls values with zeros
        self.df[col] = self.df[col].fillna(0.00)
        return self.df
