# 아래 함수를 수정하시오.
def even_elements(lst):
    result = []
    while lst: # lst 안에 원소가 하나라도 있으면 아래 코드가 실행된다. 없으면 중단
        number = lst.pop(0) # 리스트 맨 앞 원소 제거
        if number % 2 == 0 : # number 가 짝수이면
            result.extend([number])
    
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
