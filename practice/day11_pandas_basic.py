import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "study_hours" : [1,2,3,4,5],
    "sleep_hours": [5, 6, 6, 7, 8],
    "score": [50, 60, 68, 80, 90]
}

df = pd.DataFrame(data)

print("전체 데이터")
print(df)

print("앞부분 3개")
print(df.head(3))

print("-"*40)

print("데이터 정보")
print(df.info())


print("-" * 40)

print("기초 통계")
print(df.describe())

print("-" * 40)
print("X, y 분리")

X = df[["study_hours","sleep_hours"]]

y =  df["score"]



print("X 데이터")
print(X)

print("y 데이터")
print(y)


model = LinearRegression()

model.fit(X,y)

X_test = pd.DataFrame({
    "study_hours": [6, 7],
    "sleep_hours": [8, 6]
})

y_pred = model.predict(X_test)

print("-" * 40)
print("예측 결과")
print(y_pred)


y_test = [98, 100]

mse = mean_squared_error(y_test, y_pred)

print("실제 정답:", y_test)
print("평균 제곱 오차:", mse)

print("계수 : ", model.coef_)
print("절편 : ", model.intercept_)