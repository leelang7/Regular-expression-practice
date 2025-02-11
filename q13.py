
import re

text = '''APPLE APPLe APPlE APpLE ApPLE aPPLE APPle APpLe ApPLe aPPLe APplE ApPlE aPPlE AppLE aPpLE apPLE'''
          

p1 = "APPLE"
p2 = ""       # 대소문자를 무시하며 APPLE에 매칭되는 패턴을 작성해보세요.

m1 = re.findall(p1, text)
print("m1 결과 : ", m1)

m2 = re.findall(p2, text)
print("m2 결과 : ", m2)
