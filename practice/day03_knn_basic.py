
def calculate_distance(point_a, point_b):
    height_diff = point_a[0] - point_b[0]
    weight_diff = point_a[1] - point_b[1]

    distance = (height_diff ** 2  + weight_diff ** 2) ** 0.5
    return distance

train_data = [
    {"features":[170, 65],"label":"normal"},
    {"features":[180, 85],"label":"heavy"},
    {"features":[160, 50],"label":"light"},
    {"features":[172, 68],"label":"normal"},
    {"features":[182, 90],"label":"heavy"}
]

new_data = [171, 66]
distances =[]

for data in train_data:
    distance = calculate_distance(data["features"], new_data)

    distances.append({
        "distance": distance,
        "label":data["label"]
    })

print(distances)
for item in distances:
    print(item)

distances.sort(key = lambda x: x["distance"])

print("가까운 순서 : ")
for item in distances:
    print(item)

k = 5

nearest_neighbors = distances[:k]
print("가장 가까운 이웃 3개 : ")

for neighbor in nearest_neighbors:
    print(neighbor)


votes ={}

for neighbor in nearest_neighbors:
    label = neighbor["label"]

    if label not in votes:
        votes[label] = 0

    votes[label] +=1

print("투표결과 : ", votes)


prediction =  max(votes, key = votes.get)
print("예측 결과", prediction)