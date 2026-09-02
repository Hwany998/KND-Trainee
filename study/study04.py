import pandas as pd

tags = pd.read_csv('csv/03-01_유압·열설비_신호_계통태그목록.csv')
df = pd.read_csv('csv/03-01_유압·열설비_신호_유압운전.csv')

print(tags.loc[tags.startswith(['tag']) == 'HYD', ['tag','physical_qty','unit','direction']])

COL = ['HYD01_PRESS_PUMP', 'HYD01_FLOW', 'HYD01_OILTEMP', 'HYD01_LEVEL', 'HYD01_PUMP_CURRENT']

