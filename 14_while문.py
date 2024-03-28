max = 25
weight = 0
item = 3
count = 0
while weight + item <= max:
    weight += item
    count += 1
    print(f"짐을 {count}회 추가합니다")
print("짐을 더 이상 담을수 없습니다.")