decimal = 149


# 비트연산을 통해서 십진수 => 이진수로
# & 1 하면 해당비트가 1인지 아닌지 알수 있다.

def dec_to_bin(dec):
    bin = ""
    for i in range(7,-1,-1):
        # 1을 왼쪽으로 i번 밀어서 해당 비트가 1인지 아닌지 판별
        if dec & (1 << i):
            # i번째 비트에 1이 있었다면 이진수 1 추가
            bin += "1"
        else:
            bin += "0"
    print(bin)

dec_to_bin(149)
    

