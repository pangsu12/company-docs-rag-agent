from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


X_train = [
    [1],
    [2],
    [3],
    [4],
    [5]
]

y_train = [
    50,
    60,
    70,
    80,
    90
]

model = LinearRegression()

model.fit(X_train, y_train)

X_test = [
    [6],
    [7]
]

y_pred = model.predict(X_test)

print("예측 결과:", y_pred)


y_test = [
    98,
    115
]

mse = mean_squared_error(y_test, y_pred)

print("실제 정답 : ", y_test)
print("평균 제곱 오차 : ", mse)