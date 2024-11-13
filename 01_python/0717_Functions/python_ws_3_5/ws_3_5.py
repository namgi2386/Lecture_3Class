number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print('남은 책의 수 : ', number_of_book)

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(create_user, name, age, address))


def rental_book(info):
    decrease_book(info['age'])
    print(f'{info["name"]}님이 {info["age"]}권의 책을 대여하였습니다.')


# 'many_user' 리스트에 대해 람다 함수를 적용하여 사용자의 이름과 나이를 추출하고, 나이를 10으로 나눈 값을 가진 딕셔너리로 변환 후
# 'rental_book' 함수를 호출하여 각 user의 age 만큼 책의 수를 감소시킨다.
list(
    map(
        rental_book,
        map(lambda x: {'name': x['name'], 'age': x['age'] // 10}, many_user),
    )
)
