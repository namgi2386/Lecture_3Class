# 아래 함수를 수정하시오.
def count_character(word, char): 
    count = 0 # char 의 갯수

    for c in word: # word 문자열에서 글자 하나 떼어온거를 c 라고 하자
        if c == char: # c가 char 랑 같냐?
            count += 1 # 같으면 개수 증가
    
    return count


result = count_character("Hello, World!", "l")
print(result)  # 2
