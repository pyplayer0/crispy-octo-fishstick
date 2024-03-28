#   def 함수명():
#       수행할문장

# 전달값
#   def 함수명(전달값):
#       수행할문장

def show_price(customer):
    print(f"사랑하는 {customer} 고객님")
    print("커트 가격은 15,000원 입니다.")

customer1 = "김태환"
customer2 = "미친년"

show_price(customer1)
show_price(customer2)

# 반환값
#   def 함수명(전달값):
#       수행할문장
#       return 반환값
def get_price(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(f"커트 가격은 {price}원 입니다.")

# 기본값
def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000

price1 = get_price(True)
price2 = get_price()
price3 = get_price()
price4 = get_price()

# 키워드값
def get_price(is_vip=False,
              is_birthday=False,
              is_membership=False,
              card=False,
              review=False,
              first_time=False):
    pass
# ... return 할 문장이나 값
price = get_price(review=True)

# 가변인자 (마지막에 한번만 가능)
def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit("2022년 6월 12일", '나미리')
visit("2022년 6월 12일", '나미리','채송아')
visit("2022년 6월 12일", '나미리','채송아','원장님')

# 지역변수 : 함수내에서 정의된 변수 > 함수내에서만 사용가능
# 전역변수 : 어디서든지 사용가능
message = "나는야 전역변수"
print(message)

def no_secret():
    global message #global 전역변수로 사용하겠다
    message = "오 진짜 전역변수!!"

no_secret()
print(message)
