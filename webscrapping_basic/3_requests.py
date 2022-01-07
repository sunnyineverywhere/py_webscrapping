import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
print("응답 코드 : ", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상")
else:
    print("문제 [에러코드", res.status_code, "]")

res.raise_for_status()
print("웹 스크래핑 진행")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
