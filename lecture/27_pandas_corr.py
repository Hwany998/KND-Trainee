import pandas as pd

df_qc = pd.read_csv('data/14_hydraulic_qc.csv', encoding='utf-8')
df_qc.info()

r1 = df_qc['지표07'].corr(df_qc['지표08'])
print(r1) # -0.9690877323579701 강한 음의 상관관계
print(r1.round(3)) # -0.969

cols = ['지표01', '지표02', '지표03', '지표04', '지표05', 
        '지표06', '지표07', '지표08', '지표09', '지표10']
r2 = df_qc[cols].corr()
print(r2.round(3))
