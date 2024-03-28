# 조건이 True일 경우 if문내의 코드를 실행

total = 2 
if total >= 4:
    print("추가비용 없음")
else:
    print("1인당 만원")
print("감사합니다") # 추가비용 없음 감사합니다 

yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print("퇴장")
    else:
        print("옐로 카드 누적 1장")
else:
    print("주의")