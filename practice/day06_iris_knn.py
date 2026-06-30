from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris  = load_iris()

X = iris.data
y = iris.target

print("입력 데이터 개수 : ", len(X))
print("정답 데이터 개수 : ", len(y))
print("특성 이름 : ", iris.feature_names)
print("클래스 이름: ", iris.target_names)

print("-" * 40)


print("첫 번째 입력 데이터 : ", X[0])
print("첫 번째 정답: ", y[0])
print("첫 번째 정답 이름 : ", iris.target_names[y[0]])

print("-" * 40)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("학습 데이터 개수:", len(X_train))
print("테스트 데이터 개수:", len(X_test))

print("-" * 40)


model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("예측결과 : ", y_pred)
print("실제결과 : ", y_test)
print("정확도 : ", accuracy)


print("-" * 40)
print("k값별 정확도 비교")


for k in [1,3,5,7,9]:
    model = KNeighborsClassifier(n_neighbors= k)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("k : ", k ,"정확도 : ", accuracy)
