import pandas as pd
from io import StringIO

class Internet_Help:
    def CSV_Count_and_Remove_Duplicates(self):

        csv_data = """id,num1,num2,num3
        1,300,200,1121
        2,300,190,1122
        3,300,180,1123
        4,300,170,1124
        5,300,160,1125
        6,300,150,1126
        7,300,140,1127
        8,300,130,1128
        9,300,120,1129
        10,300,195,1122
        11,300,185,1122
        12,300,175,1126
        13,300,165,1122
        14,300,155,1122
        15,300,145,1122
        16,300,135,1122"""

        df = pd.read_csv(StringIO(csv_data)) # make the data frame
        # print(df)

        # aggregate results 'column : aggregate type'
        df = df.groupby('num3').agg({ 
            'id' : 'min',
            'num1': 'max',
            'num2': 'max',
            'num3': 'max',
            'num3': 'count',
        })
        df.columns = ['id', 'num1', 'num2', 'num3_count'] # rename the columns
        # print(df)

        # reorder the columns as they are stored to a csv style
        df = df.to_csv(header = True, columns = ['id', 'num1', 'num2', 'num3_count'])

        # recreate the dataframe from the new csv
        df = pd.read_csv(StringIO(df)) 

        # reorder the final output as a csv
        df = df.to_csv(index=False, header = True, columns = ['id', 'num1', 'num2', 'num3', 'num3_count'])

        print(df) # print the dataframe to console for viewing


class MaxValue():        
    def __init__(self,max_val):
        self.max_val = max_val
        
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if value <= self.max_val:
                raise ValueError(f"{self.name} must be less than {self.max_val}")
        obj.__dict__[self.name] = value       
        
        
class Demo():
    A = MaxValue(5)
    def __init__(self, A):
        self.A = A