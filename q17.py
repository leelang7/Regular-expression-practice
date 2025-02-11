import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "1 12 102 8948 754 77 3 222"

p1 = "\d+"       # 숫자 매칭
p2 = ""         # 세 자리 수 매칭

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

