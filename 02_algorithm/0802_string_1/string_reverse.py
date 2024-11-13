s = "abcdef"
# a + b + c + d + e + f
#
# f + e + d + c + b + a

# s를 뒤집기 (반복문 사용해서)
s_reverse = ""
for i in range(len(s)):
    s_reverse += s[len(s) - 1 - i]

print(s_reverse)
print(s[::-1])
