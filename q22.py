import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "catatatatatat"

p1 = "cat"
p2 = ""             # 정규식 패턴 입력!

m1 = re.search(p1, text)
m2 = re.search(p2, text)

print("m1 결과 : ", m1.group())
print("m2 결과 : ", m2.group())
