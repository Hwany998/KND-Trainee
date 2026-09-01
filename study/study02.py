import pandas as pd

df = pd.read_csv('csv/02-01_측정의_3요소_측정샘플.csv', parse_dates=["timestamp"])
print("행 개수:", len(df))
print(df.head())

# 태그 컬럼 목록 (timestamp 제외)
tag_cols = [c for c in df.columns if c != "timestamp"]


# ── [Step 2] 실제 저장 간격 확인 ───────────────────────────
# timestamp 컬럼을 한 칸씩 밀어 빼면(diff) 행 사이의 시간차가 나온다.
time_diffs = df["timestamp"].diff().dropna()

print("\n[Step 2] 타임스탬프 간격")
print("발견된 간격 종류:", time_diffs.unique())
print("모든 행이 같은 간격인가?:", time_diffs.nunique() == 1)
print("간격(초):", time_diffs.dt.total_seconds().iloc[0])


# ── [Step 3] 값의 크기와 움직임 확인 ────────────────────────
print("\n[Step 3] 태그별 최솟값 / 최댓값 / 평균 / 최소 변화폭")

for col in tag_cols:
    values = df[col]

    vmin = values.min()
    vmax = values.max()
    vmean = values.mean()

    # 값이 변한 최소 폭: 앞 행과의 차이(diff)를 구한 뒤
    # 0이 아닌(=값이 실제로 바뀐) 차이들 중 가장 작은 절댓값
    diffs = values.diff().dropna()
    nonzero_diffs = diffs[diffs != 0].abs()
    min_change = nonzero_diffs.min() if len(nonzero_diffs) > 0 else None

    print(f"{col:18s} | min={vmin:<9} max={vmax:<9} "
          f"mean={round(vmean, 2):<9} min_change={min_change}")


# ── 계단식(staircase) 패턴 찾기 ─────────────────────────────
# 같은 값이 연속으로 반복되는 비율이 높을수록 "계단처럼" 변하는 태그다.
print("\n[참고] 연속으로 값이 그대로 유지된 비율 (높을수록 계단식)")
for col in tag_cols:
    values = df[col]
    same_as_prev = (values.diff() == 0).sum()
    ratio = same_as_prev / (len(values) - 1)
    print(f"{col:18s} | 값 유지 비율={ratio:.2%}")