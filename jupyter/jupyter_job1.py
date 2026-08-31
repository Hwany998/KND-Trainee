import pandas as pd

df = pd.read_csv("csv/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape) #(720행, 6열)

print(df[['blast_flow_nm3min', 'blast_pressure_kpa', 'blower_vib_mms']].describe().round(1))
print('-' * 40)

front_area = df.iloc[:360]
back_area = df.iloc[360:]

cols = ['blast_flow_nm3min', 'blast_pressure_kpa', 'blower_vib_mms']
print(front_area[cols].mean())
print(back_area[cols].mean())

for arr in cols:
    if front_area[arr].mean() > back_area[arr].mean():
        print("앞승")
    else:
        print("뒷승")
# print(df["f_flow_ma"].head(3).tolist())   #[nan, nan, nan]    #평균 구하려면 15분이 필요하니까 15개까지는 nan값
# print(df["b_flow_ma"].head(3).tolist())   #[nan, nan, nan]    #평균 구하려면 15분이 필요하니까 15개까지는 nan값