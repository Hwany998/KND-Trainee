import pandas as pd

df = pd.read_csv('csv/13_diecasting_small.csv')
df.info()

df['형체력'].info() #Series
df[['형체력', '실린더압력']].info() #DataFrame