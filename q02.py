
import re

text = "abcdefg"

pattern = re.compile("e")

print("정규식 객체의 자료형 : ", type(pattern))

print("정규식 객체 사용하는 경우 : ", pattern.findall(text))

print("객체를 사용하지 않는 경우 : ", re.findall("e", text))
