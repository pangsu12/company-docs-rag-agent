import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("practice/student_scores.csv")

print("CSV 데이터")
print(df)


print("-" * 40)

X = df[["study_hours", "sleep_hours"]]
y= df["score"]

X_train = X.iloc[:5]
y_train = y.iloc[:5]

X_test = X.iloc[5:]
y_test = y.iloc[5:]


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print("예측 결과:", y_pred)
print("실제 정답:")
print(y_test)
print("평균 제곱 오차:", mse)

print("계수:", model.coef_)
print("절편:", model.intercept_)