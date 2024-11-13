class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    pass
    # A1. 생성자를 직접 정의하지 않으면 파이썬이 실행할 때 아래처럼 만들어서 사용
    # def __init__(self):
    #     super().__init__()

# Q1. Parent 의 __init__ 호출한적 없는데 왜 "Parent init" 찍히는 걸까
c1 = Child()

# Q2. __str__ __ge__ 이런거 만든적 없는데 어디서 났을까?
print(dir(c1))

# A2. 파이썬의 모든 클래스는 기본적으로 object 클래스를 상속받는다.
# object 클래스는 파이썬의 최상위 클래스라 할 수 있음.
# 매직 메서드들은 다 object 클래스 안에 있던것을 상속받아서 사용
print(dir(object()))