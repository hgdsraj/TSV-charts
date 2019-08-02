import pandas as pd


file_name = 'chart.tsv'
df=pd.read_csv('myfile.csv', sep='\t',header=None)
print(df)
