# 두 데이터 사이의 거리를 계산하는 함수
def calculate_distance(point_a, point_b):
    height_diff = point_a[0] - point_b[0]
    weight_diff = point_a[1] - point_b[1]

    distance = (height_diff ** 2  + weight_diff ** 2) ** 0.5
    return distance

# 학습 데이터: features는 입력값, label은 정답
train_data = [
    {"features":[170, 65],"label":"normal"},
    {"features":[180, 85],"label":"heavy"},
    {"features":[160, 50],"label":"light"},
    {"features":[172, 68],"label":"normal"},
    {"features":[182, 90],"label":"heavy"}
]

#분류 하려는 새 데이터  
new_data = [174,70]
# 각 학습 데이터와 새 데이터 사이의 거리 및 label을 저장할 리스트
distances =[]

# 학습 데이터를 하나씩 꺼내 새 데이터와의 거리를 계산한다

for data in train_data:
    distance = calculate_distance(data["features"], new_data)
    # 계산한 거리와 해당 데이터의 label을 함께 저장한다
    distances.append({
        "distance": distance,
        "label":data["label"]
    })

print(distances)
# distance 값을 기준으로 가까운 순서대로 정렬한다
distances.sort(key = lambda x: x["distance"])

print("가까운 순서 : ")
for item in distances:
    print(item)

k = 3
# 가장 가까운 k개의 이웃만 선택한다
nearest_neighbors = distances[:k]
print("가장 가까운 이웃 3개 : ")

for neighbor in nearest_neighbors:
    print(neighbor)

# label별 투표 수를 저장할 딕셔너리
votes ={}
# 가까운 이웃들의 label 개수를 센다
for neighbor in nearest_neighbors:
    label = neighbor["label"]
    # 처음 나온 label이면 0으로 초기화한다
    if label not in votes:
        votes[label] = 0
    # 해당 label의 투표 수를 1 증가시킨다
    votes[label] +=1

print("투표결과 : ", votes)

# 가장 많이 투표받은 label을 예측 결과로 선택한다
prediction =  max(votes, key = votes.get)
print("예측 결과", prediction)