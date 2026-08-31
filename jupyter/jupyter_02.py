import pandas as pd

df = pd.read_csv("csv/01-02_원료_전처리와_제선_제선조업.csv")
print(df.shape) #(720행, 6열)

#timestamp열 데이터 타입 확인하기
print("timestamp 데이터 타입(1):", df["timestamp"].dtype)  #str
df["timestamp"] = pd.to_datetime(df["timestamp"])
print("timestamp의 데이터 타입(2):", df["timestamp"].dtype) #datetime64[us]

#2. read_csv() 의 옵션값 이용
df = pd.read_csv("csv/01-02_원료_전처리와_제선_제선조업.csv", parse_dates = ["timestamp"])
print("timestamp의 데이터 타입(3):", df["timestamp"].dtype) #datetime64[us]

#timestamp의 시간 간격
gaps = df['timestamp'].diff().value_counts()
print(gaps)

'''
timestamp
0 days 00:01:00    719      0부터 719까지 1분 간격이다 (720개 열 시간 간격)
Name: count, dtype: int64   
'''

#송풍량, 송풍압, 송풍기 진동
print(df[['blast_flow_nm3min', 'blast_pressure_kpa', 'blower_vib_mms']].describe().round(1))
'''
       blast_flow_nm3min  blast_pressure_kpa  blower_vib_mms
count              720.0               720.0           720.0
mean              5088.2               388.8             3.4
std                159.6                13.0             0.1
min               4681.8               372.8             3.2
25%               4977.5               379.4             3.3
50%               5180.8               381.7             3.4
75%               5202.5               398.3             3.4
max               5258.2               421.4             3.6
'''

# 이동 평균: n분간의 흔들림을 확인하여 송풍량의 장기적인 방향을 보는 지표
# 통기성이 나빠지면 공기가 원료층을 통과하기 어려워져서 실제 들어가는 풍량이 감소할 수 있다.

df["flow_ma"] = df["blast_flow_nm3min"].rolling(window=15).mean()   #15분 간격 이동평균 구하기
print(df["flow_ma"].head(3).tolist())   #[nan, nan, nan]    #평균 구하려면 15분이 필요하니까 15개까지는 nan값

print(round(df['flow_ma'].iloc[14], 1), round(df['flow_ma'].iloc[400], 1))  #5201.5, 5200.8
# 차이가 크지 않기에 통기성 악화가 보이지 않음

#이동표준편차
df['top_sd'] = df['top_pressure_kpa'].rolling(window=30).std()
print(round(df['top_sd'].iloc[200], 2), round(df['top_sd'].iloc[560], 2))   #2.64 4.28
