from sklearn.neighbors import KNeighborsClassifier

X_train = [
    [170, 65],
    [180, 85],
    [160, 50],
    [172, 68],
    [182, 90],

]

y_train = [
    "normal",
    "heavy",
    "light",
    "normal",
    "heavy",
]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

new_data = [[174, 70]]

prediction = model.predict(new_data)

print("예측 결과", prediction[0])

test_samples = [
    [181, 88],
    [161, 52],
    [171, 66],
    [174, 70],
]

predictions = model.predict(test_samples)

for sample, prediction in zip(test_samples, predictions):
    print("입력 : ", sample, "결과 : ", prediction)

print("-"*40)

for k in [1, 3, 5]:
    model = KNeighborsClassifier(n_neighbors= k)
    model.fit(X_train, y_train)

    prediction = model.predict(test_samples)

    print("k = ", k)

    for sample, prediction in zip(test_samples, predictions):
        print("입력 : ", sample, "결과 : ", prediction)

    print()