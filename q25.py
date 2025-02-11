import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "tomato potato"

p1 = "(tom|pot)ato"    # tomato 또는 potato와 매칭하자
p2 = ""                # 올바른 패턴을 작성해보세요.

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

