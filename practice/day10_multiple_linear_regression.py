from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


X_train = [
    [1, 5],
    [2, 6],
    [3, 6],
    [4, 7],
    [5, 8]
]

# y = 시험 점수
y_train = [
    50,
    60,
    68,
    80,
    90
]

model = LinearRegression()

model.fit(X_train,y_train)

X_test = [
    [6, 8],
    [7, 6]
]

y_pred = model.predict(X_test)

print("예측 결과:", y_pred)

y_test = [
    98,
    100
]

mse = mean_squared_error(y_test, y_pred)

print("실제 정답:", y_test)
print("평균 제곱 오차:", mse)
print("계수 : ", model.coef_)
print("절편 : ", model.intercept_)
