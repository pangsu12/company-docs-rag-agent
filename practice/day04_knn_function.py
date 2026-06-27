def calculate_distance(point_a, point_b):
    hight_diff = point_a[0] - point_b[0]
    weight_diff = point_a[1] - point_b[1]

    distance = (hight_diff **2  + weight_diff ** 2) ** 0.5
    return distance

def predict_knn(train_data, new_data, k):
    distances = []

    for data in train_data:
        distance = calculate_distance(data["features"], new_data)

        distances.append({
            "distance": distance,
            "label": data["label"]
        })

    distances.sort(key = lambda x: x["distance"])

    nearest_neighbors = distances[:k]
    votes = {}

    for negihbor in nearest_neighbors:
        label = negihbor["label"]

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