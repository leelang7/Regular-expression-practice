import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "cat bat c@t hat cut com cook cant"

p1 = ""        # c로 시작하고 t으로 끝나는, 모든 3글자 단어에 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)
