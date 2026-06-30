import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("practice/student_scores_missing.csv")

print("원본 데이터")
print(df)


print("-" * 40)
print("결측치 확인")
print(df.isnull())

print("-" * 40)

print("컬럼별 결측치 개수")
print(df.isnull().sum())

print("-" * 40)
print("결측치 있는 행 제거")

df_drop = df.dropna()
print(df_drop)

print("-" * 40)
print("결측치 평균값으로 채우기")

df_fill = df.copy()

df_fill["sleep_hours"] =df_fill["sleep_hours"].fillna(df_fill["sleep_hours"].mean())
df_fill["score"] =df_fill["score"].fillna(df_fill["score"].mean())

print(df_fill)

print("-" * 40)
print("전처리 후 머신러닝")

X = df_fill[["study_hours","sleep_hours"]]
y = df_fill["score"]

X_train = X.iloc[:5]
y_train = y.iloc[:5]

X_test = X.iloc[5:]
y_test = y.iloc[5:]
model = LinearRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print("예측 결과:", y_pred)
print("실제 정답:")
print(y_test)
print("평균 제곱 오차:", mse)
print("계수:", model.coef_)
print("절편:", model.intercept_)