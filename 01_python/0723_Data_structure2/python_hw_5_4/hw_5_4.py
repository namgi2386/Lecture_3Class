# 아래 함수를 수정하시오.
def find_min_max(lst):
    min_v = lst[0] # 최소값
    max_v = lst[0] # 최대값

    for num in lst: 
        if num < min_v: # 이전에 내가 알던 최소값보다 작은 값을 발견
            min_v = num # 작은 값으로 최소값을 갱신
        if num > max_v: # 이전에 내가 알던 최대값보다 큰 값을 발견
            max_v = num # 큰 값으로 최대값을 갱신
    
    return min_v, max_v

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
