tema = "티아라멘츠"
tema_monster = ["메이루", "허프니스", "세이렌", "키토칼로스", "루루칼로스"]
heart_monster = ["레이노하트", "카레이드하트"]

print(tema_monster[:1])
print("메이루" in tema_monster)
print(len(tema_monster))
tema_monster.remove("메이루")
print(tema_monster)
tema_monster.append("메이루") # append로 list를 넣을 경우 전체가 하나의 객체가 된다 
print(tema_monster) #ex) [1,2,3,4,[1,2,3]] < 이런느낌
tema_monster.extend(heart_monster) # 그래서 extend를 사용해준다
print(tema_monster)

# list comprehension
# new_list = [변수활용 for 변수 in 반복대상 if 조건]
my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x < 4]
print(new_list)