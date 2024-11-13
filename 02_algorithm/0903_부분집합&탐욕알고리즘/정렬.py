# (무게(kg), 가치) 
arr = [(10, 60), (5, 50), (20, 140)]


# kg당 가치를 기준으로 정렬

# 단순한 한개의 값이 아닌 여러개의 값을 가진 구조를 정렬
# 이 여러개의 값들 중에 우리가 사용하고 싶은 정렬 기준이 뭔가??

# 정렬 기준이 기본적으로 제공되는 타입들(숫자, 문자열..) 이외에
# 것들은 우리가 직접 정렬 기준을 정해주어야 한다.
# sort() 함수의 key 인자를 활용해서 어떤 값을 기준으로 정렬 할지 함수로 작성

# x : arr안의 있는 원소 하나(단순한 값이 아니라 복잡한 값)
def myfunction(x):
    # x의 kg당 가치를 기준으로 정렬해라.
    return x[1] // x[0]


# arr.sort(key=myfunction, reverse=True)
arr.sort(key=lambda x: x[1] // x[0], reverse=True)
print(arr)
