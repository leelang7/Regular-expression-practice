
import re

text = '''&7q:>@6j`~itIghnfHH8=FW7y?<g"lt?=q3*kJdN/bsrF()Z<U$_w2-`KUnyxLB<8uMm%*`"[:%yha[f`bEXHW=qD9K>95K92cvI>Kj51/cy~cwaN[jB'u5<Ix8?;y~g15T_bb2z<uL&xOIaMJFk>s^}nz.sWx<2)R?:x5r9,T_45]zQ>Z|FN%AFf/#@^FR#&wogd@hlk(7&MZqqurTF+V5oy`cpM.iMUBMd#wGs9RTj7J`Q=,AIv3x%&/Q)-jDk'''
          

p = ""  # 9행의 re.compile 함수에 들어갈 문자열 매개변수입니다.

m = re.findall(p, text)
print("결과 : ", m)
