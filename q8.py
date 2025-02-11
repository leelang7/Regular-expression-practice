import re

### 아래 p2과 p3에 직접 정규표현식을 입력해보세요.

p1 = "a|e|i|o|u"     # 알파벳 모음에 매치
p2 = ""     # 알파벳 모음에 매치
p3 = ""     # 알파벳 모음이 아닌 문자(자음)에 매치

m1 = re.findall(p1, "Life is short, art is long")
m2 = re.findall(p2, "Life is short, art is long")
m3 = re.findall(p3, "Life is short, art is long")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
print("m3 결과 : ", m3)
