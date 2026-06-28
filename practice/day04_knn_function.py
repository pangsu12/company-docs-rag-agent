def calculate_distance(point_a, point_b):
    height_diff = point_a[0] - point_b[0]
    weight_diff = point_a[1] - point_b[1]

    distance = (height_diff ** 2 + weight_diff ** 2) ** 0.5
    return distance


def predict_knn(train_data, new_data, k):
    distances = []

    for data in train_data:
        distance = calculate_distance(data["features"], new_data)

        distances.append({
            "distance": distance,
            "label": data["label"]
        })

    distances.sort(key=lambda x: x["distance"])

    nearest_neighbors = distances[:k]

    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor["label"]

        if label not in votes:
            votes[label] = 0

        votes[label] += 1

    prediction = max(votes, key=votes.get)
    return prediction


train_data = [
    {"features": [170, 65], "label": "normal"},
    {"features": [180, 85], "label": "heavy"},
    {"features": [160, 50], "label": "light"},
    {"features": [172, 68], "label": "normal"},
    {"features": [182, 90], "label": "heavy"}
]

new_data = [190, 70]

result = predict_knn(train_data, new_data, k=3)

print("예측 결과:", result)

test_samples = [
    [181, 88],
    [161, 52],
    [171, 66],
    [174, 70]
]

for sample in test_samples:
    result = predict_knn(train_data, sample, k=3)
    print("입력:", sample, "예측:", result)


print("-" * 40)
print("여러 입력에 대한 k 값 비교")

test_samples = [
    [174, 70],
    [181, 88],
    [161, 52],
    [175, 78]
]

for sample in test_samples:
    print("입력:", sample)

    for k in [1, 3, 5]:
        result = predict_knn(train_data, sample, k)
        print("  k:", k, "예측:", result)

    print()