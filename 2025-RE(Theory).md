## [이론1] 파이썬의 re 모듈



여러 프로그래밍 언어에서는 문자열과 관련된 라이브러리를 많이 제공합니다. 그럼에도 불구하고 여러분이 정규표현식을 꼭 배워야 하는 이유는 무엇일까요?

여러분에게 다음과 같은 문제가 주어졌다고 생각해보세요.

> 보안을 위해 고객 정보 중 전화번호 가운데 자리의 숫자는 `*` 문자로 변경하세요.

고객 정보는 이름, 주민번호, 전화번호가 문자열 데이터로 주어진다고 가정해봅시다.

```
text = '''
Elice 123456-1234567 010-1234-5678
Cheshire 345678-678901 01098765432
'''
```

이 문제를 정규식을 사용하지 않고 풀려면 매우 복잡하게 풀어야 합니다.

1. 전체 텍스트를 공백 문자를 기준으로 나눈다.
2. 나누어진 문자열이 전화번호 형식인지 점검한다.
3. 전화번호를 다시 나누어 가운데 자리의 숫자를 `*`로 변환한다.
4. 나눈 문자열을 다시 합쳐 전화번호를 완성한다.

그런데 나누어진 문자열을 전화번호 형식인지 어떻게 점검할까요? 그리고 가운데 자리의 숫자는 어떻게 나누어 `*`로 변환하고 다시 합칠까요?

설상가상으로 전화번호의 구분문자인 `-`도 있기 때문에 문제 해결은 더욱 쉽지 않습니다.

그러나 정규표현식을 이용하면 매우 간편하게 코드를 작성할 수 있습니다.

### ***\*Let's go!\****

앞서 예로 든 전화번호같이, 원하는 형식의 문자열을 검색할 때 메타문자와 수량자 등 다양한 ***\*패턴\****을 사용하여 매치하고, 그룹핑을 이용하여 원하는 부분만 골라내고 `re`모듈의 메서드로 문자열을 수정할 수도 있습니다.

위 개념들은 모두 이번 과목에서 다루는 내용들입니다.

정규표현식을 배우고 활용할 수 있는 실력을 키워보세요!



## [이론2] **메타 문자란?**

메타 문자는 특정한 문자 혹은 계열을 표현하는 약속된 **기호** 입니다. 메타 문자를 이용하면 특정한 규칙을 가진 여러 단어를 짧게 압축할 수 있어 편리합니다.

1장 실습에서는 문자열 변수에서 특정 문자열과 메타 문자로 패턴을 구성하여 검색하고자 하는 부분을 추출하는 실습을 진행합니다.

메타 문자는 아래와 같이 구성되어 있습니다.

| 메타 문자 | 의미                                                         | 예시                                                         |
| :-------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| ^         | 문자열의 시작                                                | `^www`는 문자열의 맨 처음에 `www`가 오는 경우에 매치합니다.  |
| $         | 문자열의 끝                                                  | `.com$`은 문자열의 맨 끝에 `.com`이 오는 경우에 매치합니다.  |
| \|        | or 조건식                                                    | 여러 가지 중 하나와 일치하면 매치합니다. `Apple|Banana`는 `Apple`과 `banana`에 모두 매치됩니다. |
| []        | 문자 클래스                                                  | 대괄호 `[]` 안에 들어있는 문자 중 하나라도 일치하면 매치합니다.`[abc]`는 ‘a,b,c’ 중 하나와 매칭됩니다. |
| \d        | 숫자를 나타냅니다.                                           |                                                              |
| \D        | 숫자가 아닌 모든 문자를 나타냅니다.                          |                                                              |
| \w        | 알파벳 대소문자, 숫자, 밑줄(`_`)을 나타냅니다.               |                                                              |
| \W        | \w에 해당되지 않는 문자들을 나타냅니다.                      |                                                              |
| \s        | 공백, 탭 문자와 매칭됩니다.                                  |                                                              |
| \S        | \s에 매칭되지 않는 모든 문자를 나타냅니다.                   |                                                              |
| \n        | 개행 문자를 나타냅니다.                                      |                                                              |
| \         | 이스케이프용 문자. 특별한 의미를 나타내는 기호를 문자 그대로 나타내려고 할 때 사용합니다. | 문자열 내에서 `$`문자를 찾기 위해서는 `\$`와 같이 나타내어야 합니다. |
| .         | 모든 문자와 대응되는 기호입니다.                             |                                                              |



## [이론3] **수량자란?**

동일한 글자나 패턴이 반복될 때, 그대로 정규표현식을 만들고자 하면 상당히 불편합니다.

\d와 \w를 이용하면 각각 숫자와 문자를 한 글자씩 매칭해주는데요, 이어지는 문자를 패턴으로 만들어, 단어 단위로 매칭하고 싶을 때엔 상당히 불편합니다.

이런 상황에서 유용하게 사용할 수 있는 수량자를 배워봅시다.

| **수량자** | **의미**           | **예시**                                                     |
| :--------- | :----------------- | :----------------------------------------------------------- |
| *          | 0개 이상           | `elice*`는 “elic”, “elice”, “elicee”, “eliceee…eee”와 매칭됩니다. |
| +          | 1개 이상           | `*`와는 달리, 적어도 해당 문자가 1개 이상이어야 매칭됩니다.  |
| ?          | 0개 또는 1개       | `elice?`는 “elic”, “elice”와 매칭됩니다.                     |
| {n}        | n개                | `\d{3}`은 123, 456 등 세 자릿수와 매칭됩니다.                |
| {n, m}     | n개 이상, m개 이하 | `\w{3, 5}`는 알파벳 세 자리에서 다섯 자리의 단어와 매칭됩니다. |
| {n,}       | n개 이상           | `a{4,}`는 a가 최소 4개 이상 연속된 경우에 매칭됩니다.        |



## [이론4] 그룹이란?

괄호는 그룹을 나타냅니다. 그룹은 전체 패턴 내에서 하나로 묶여지는 패턴을 말합니다. 그룹과 `|`를 결합한 형태, 또는 그룹 뒤에 수량자를 붙이는 패턴으로 자주 사용됩니다.

### **예시**

- `(e|a)lice` 는 `elice`, `alice`와 매칭됩니다.
- `(tom|pot)ato`는 `tomato`, `potato`와 매칭됩니다.
- `(base|kick){2}` 은 `basebase`, `basekick`, `kickkick`, `kickbase` 와 매칭됩니다.

### **그룹의 재사용**

한 번 만든 그룹은 재사용할 수도 있습니다. 만들어진 순서부터 1번부터 시작하는 그룹으로 참조할 수 있는데, 매치한 그룹을 패턴 내에서 재사용하려면 `\\1`과 같이 그룹 번호를 이스케이프하여 나타내야 합니다.

### **예시**

- `(to)ma\\1`은 `tomato`와 매칭됩니다. 괄호를 사용하여 앞에서 만든 그룹 `(to)`를 뒤에서 재사용하는 모습입니다.

### **그 외**

이외에도 그룹에는 `re` 모듈의 `match` 객체에 속해있는 group 메서드를 이용하여 매칭된 결과 중 일부 내용만을 추출할 수 있는 등 다양한 사용법이 있습니다.