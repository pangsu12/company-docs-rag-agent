from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test =  train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state= 42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("예측결과: ",y_pred)
print("실제 정답 : ", y_test)
print("정확도 : ", accuracy)


print("-" * 40)
print("max_depth별 정확도 비교")

for depth in [1,2,3,4,5,None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test,y_pred)

    print("max_depth : ", depth, "정확도 : ", accuracy)
print("-" * 40)
print("첫 번째 테스트 데이터 확인")

print("입력 데이터:", X_test[0])
print("실제 정답 번호:", y_test[0])
print("실제 정답 이름:", iris.target_names[y_test[0]])
print("예측 정답 번호:", y_pred[0])
print("예측 정답 이름:", iris.target_names[y_pred[0]])

