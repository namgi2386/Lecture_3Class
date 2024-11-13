# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0 # 클래스 변수

    # 인스턴스가 생성될때 실행되는 메서드
    def __init__(self, name):
        self.name = name
        Myth.type_of_myth += 1 # 클래스 변수는 클래스 이름을 통해 접근
    
    @staticmethod
    def description():
        print("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.")

dangun = Myth("dangun")
greek = Myth("greek & rome")

print(dangun.name)
print(greek.name)
print(f"현재까지 생성된 신화 수 : {Myth.type_of_myth}")
Myth.description()
