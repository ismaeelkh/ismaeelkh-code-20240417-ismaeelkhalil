import pandas as pd


class Data_Validation:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_negative_values(self, col : str = ''):
        # Method to check negative values
        return (self.df[col] < 0).any()
    
    def change_to_absolute(self, col: str = ''):
        # Change negative values in the specified column to their absolute values
        if self.check_negative_values(col):
            self.df[col] = self.df[col].abs()
            return "Negative prices changed to positive"
        return  "No changes" 


    def drop_zero_winner_price(self, col: str = ''):
        # Drop rows where the winner_price is zero
        initial_count = len(self.df)
        self.df = self.df[self.df[col] != 0].reset_index(drop = True)
        final_count = len(self.df)
        return initial_count - final_count
    
    def drop_above_maximum(self):
        # Drop rows where winner_price exceeds maximum_price_allowed
        initial_count = len(self.df)
        self.df = self.df[self.df['winner_price'] <= self.df['maximum_price_allowed']]
        final_count = len(self.df)
        return initial_count - final_count 
    

    def duplicates(self, col: str = ''):
        # Method to return duplicates per column
        return self.df[col].duplicated().sum()
    

    def dedup(self, col: str = ''):
        # Method to drop duplicates based on column
        if self.duplicates(col = col) > 0:
            self.df = self.df.drop_duplicates(subset = [col]).reset_index(drop = True)
        else:
            pass
        return self.df

