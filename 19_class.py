# class 클래스명:
    # 정의

class BlackBox:
    def __init__(self,name,price):
        self.name = name # 멤버변수
        self.price = price # 멤버변수

b1 = BlackBox('까망이', 200000)
print(b1.name,b1.price)

b2 = BlackBox('망이', 300000)
print(b2.name,b2.price)
