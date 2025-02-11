import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "ct cat caat caaat caaaaat caaaaaat cbt c1t c@t c_t"

p1 = ""         # c와 t 사이에 'a'가 0개 이상 있는 경우 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)
