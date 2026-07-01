import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



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

# score가 80 이상이면 pass, 아니면 fail
df["result"] =df["score"].apply(lambda x: "pass" if x >= 80 else "fail")

print("result 컬럼 추가")
print(df)

print("-"*40)

X = df[["study_hours", "sleep_hours"]]

# 정답 데이터 y
y = df["result"]

print("X 데이터")
print(X)

print("-" * 40)

print("y 데이터")
print(y)

print("-" * 40)

# 학습용 / 테스트용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("X_test")
print(X_test)

print("-" * 40)

print("y_test")
print(y_test)

print("-" * 40)

# Logistic Regression 모델 생성
model = LogisticRegression()

# 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("예측 결과:", y_pred)
print("실제 정답:")
print(y_test)
print("정확도:", accuracy)