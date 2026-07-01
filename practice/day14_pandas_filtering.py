import pandas as pd


data = {
    "name" :["kim", "lee", "park", "choi", "jung", "kang"],
    "study_hours": [1, 3, 5, 6, 2, 7],
    "sleep_hours": [5, 6, 8, 7, 4, 6],
    "score": [50, 68, 90, 92, 55, 100]
}

df = pd.DataFrame(data)

print("전체 데이터")
print(df)

print("-" * 40)
print("80점 이상 학생")

high_score = df[df["score"] >= 80]

print(high_score)

print("-" * 40)
print("공부 시간이 5시간 이상인 학생")

high_worker = df[df["study_hours"] >= 5]

print(high_worker)

print("-" * 40)
print("공부 5시간 이상이고 점수 80점 이상")

filtered = df[
    (df["score"] >= 80)&
    (df["study_hours"] >= 5)
]
print(filtered)

print("-" * 40)
print("pass 컬럼 추가")

df["pass"] = df["score"] >= 80
print(df)
print("-" * 40)
print("result 컬럼 추가")

df["result"] = df["score"].apply(lambda x: "pass" if x >= 80 else "fail")

print(df)

print("-" * 40)
print("pass 컬럼 삭제")


df_removed = df.drop(columns=["pass"])

print(df_removed)