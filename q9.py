import re

# 임의의 문자열입니다.
text = "vkvJZZjgsr=B5Al83+#@04?+p%x7DI3k"

p1 = ""     # 숫자와 매칭됨
p2 = ""     # 알파벳 소문자와 매칭됨

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

