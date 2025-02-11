import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "apple banana carrot rabbit"

p1 = "[a-z]"        # 영어 소문자 매칭
p2 = ""             # 영단어 단위로 매칭

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

