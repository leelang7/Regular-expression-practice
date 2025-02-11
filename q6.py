import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = ""         # short으로 끝나야 매치
p2 = ""         # short으로 끝나야 매치

m1 = re.findall(p1, "Life is short")
m2 = re.findall(p2, "Life is short, art is long")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
