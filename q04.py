
import re

text = '''j<Q'T~K_5f_&VO_):Igq:=8t9qPGVB&-=9;oC7$7bw>I6)=abcQiZ&nNj2J\|0'aE*QyyelicebcW:y`y#Y&nY.gq.-0m\w2m8<1<`P:`OdE{>SF}]4_"8'Ozv:}Pc5@H91j250^H,W$~GD>;K[r_3VW?pS2U*uz`lxne`,ZMeliceFJDhMf$NxcQ[K_o4=Q2z?%[Ak1Do!E!8:>)7abcprcNIelice.mT<Cwy!~T/QfD0L&V&'\$z;7$@By&8L[8?0a4=v4uYY=IK#4{vB46delice$^EI}vD*ndR{F#EJyMHIe2QK,u"c^1d32Cvl%]Hq-;+(O/M8X-ykfelicedll3nfIn>%9i*e!9[u4$W3ASbY!h1elicedg{A|lrKJsSvJ<;A*9f_7K<?elice9MGo1Ngu~5w@EL!QMKaxUS]C6##~OBiduA]wa=pIse%E=PenU<&>w_sd{eaM0elicekr=%C^^@#j[~O!7K(^^LzS(mK"f3?p|C*;`~F|0uMCS1c=Sa-ya7?8j.!9r}YZxv'''
          

p = ""  # 9행의 re.compile 함수에 들어갈 문자열 매개변수입니다.

m = re.findall(p, text)
print("결과 : ", m)
