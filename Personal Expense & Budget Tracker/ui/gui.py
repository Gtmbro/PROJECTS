import os
import pandas as pd

class Expenses:
    def __init__(self, file_name=filename):
        self.filename = file_name
        self.index = None
        self.date = None
        self.category = None
        self.amount = None
        self.notes = None

        if not os.path.exists(filename):
            with open(f"{self.filename}",'w') as f:
                f.write("Index,Date,Category,Amount,Note\n")

    def add_entry(self, index, date, category, amount, notes):
        self.index = index
        self.date = date
        self.category = category
        self.amount = amount
        self.notes = notes
        
    def edit_entry(self, index_count, column_name, new_value):
        df = pd.read_csv(self.filename)

        df.loc[df["Index"] == index_count, column_name ] = new_value

        df.to_csv(self.filename, index=False)
        
        value = df.loc[index_count-1, column_name]

    def create_file(self):
        with open(self.filename,'a') as f:
            f.write(f"{self.index},{self.date},{self.category},{self.amount},{self.notes}\n")
