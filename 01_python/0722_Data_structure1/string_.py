# 공백 문자로 구분되는 문자열"
s = "1 2 3 4 5 6 7 8 9 10"
# s = input()

# 공백 문자(" ")를 구분자(separator)로 하여 문자열 분리 후 리스트로 반환
s_to_list = s.split()

# map( int , s_to_list )
# 우리가 필요한건 문자열이 아니라 숫자이므로 리스트의 모든 요소에 int() 함수 적용
s_to_int_list = list(map(int, s_to_list))

print(s_to_int_list)

# 문자열 한줄 입력받아서 숫자 배열로 바꾸기
# data = list(map(int, input().split()))

print(s_to_list)
# 리스트를 다시 문자열로 바꾸기 => join
# 구분자.join(리스트)
s2 = "".join(s_to_list)
print(s2)


