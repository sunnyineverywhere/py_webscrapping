# regular expression

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave...

p = re.compile("ca.e")
# . : 하나의 문자를 의미
# ^ : 문자열의 시작을 의미
# $ : 문자열의 끝을 의미

m = p.match("good care")
# print(m.group()) # 매치되지 않으면 에러 발생. 매치되면 group 함수에서 출력을 해준다


def print_match(m):
    if m:
        print(m.group())  # 일치하는 문자열
        print(m.string)  # 입력받은 문자열
        print(m.start())  # 일치하는 문자열의 시작
        print(m.end())  # 일치하는 문자열의 끝
        print(m.span())  # 일치하는 문자열의 시작 / 끝
    else:
        print("not matched")


print_match(m)

m = p.search("good care")  # search : 주어진 문자열중에 매치되는 게 있는지 확인함
print_match(m)

lst = p.findall("careless care cafe")  # findall : 일치하는 모든 것을 ㅣ스트 형태로 반환
print(lst)
