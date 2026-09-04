import pandas as pd

df = pd.read_csv("csv/05-02_라벨설계_한계사례.csv")

print(df.info())
print(df)

print("\nL1")
print(df[df["case_id"] == "L1"])

print("\nL2")
print(df[df["case_id"] == "L2"])

print("\nL3")
print(df[df["case_id"] == "L3"])

print("\nL4")
print(df[df["case_id"] == "L4"])