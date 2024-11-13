N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(N): # i가 0 부터 8까지 반복
    arr_1.append(data_1[i]) # data_1의 i번째 인덱스 원소 arr_1에 추가
print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = list(map(int, data_2.split()))
for i in arr_2:
    if i % 2:
        print(i)

# if "":
#     print("이것은 True로 취급된다.")
# else:
#     print("이것은 False로 취급된다")