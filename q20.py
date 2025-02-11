import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "ac abc abbc abbbc abbbbbc"

p1 = ""         # ac, abc와 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

