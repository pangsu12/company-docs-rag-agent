import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = {
     "name": ["kim", "lee", "park", "choi", "jung", "kang", "yoon", "han", "seo", "moon"],
    "study_hours": [1, 3, 5, 6, 2, 7, 4, 8, 3, 6],
    "sleep_hours": [5, 6, 8, 7, 4, 6, 7, 8, 5, 6],
    "score": [50, 68, 90, 92, 55, 100, 78, 98, 65, 88]
}

df = pd.DataFrame(data)

print("전체 데이터")
print(df)

print("-" * 40)

X = df[["study_hours","sleep_hours"]]
y = df["score"]



X_train , X_test, y_train , y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)


print("X_train")
print(X_train)

print("-" * 40)
print("X_test")
print(X_test)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_absolute_error(y_test, y_pred)

print("-"*40)
print("예측 결과 : ", y_pred)
print("실제 정답 : ", y_test)

print("평균 제곱 오차 : ", mse)

print("계수 : ", model.coef_)
print("절편 : ", model.intercept_)