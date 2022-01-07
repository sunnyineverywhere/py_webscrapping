import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)  # soup  객체를 통해 html tag 객체에 접근
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
# attrs = attributes, 속성
print(soup.a["href"])  # a alement의 herf 속성

print(soup.find("a", attrs={"class": "Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank1.parent)
rank2 = rank1.find_next_sibling("li")  # 줄바꿈이 있어서 next_sibling을 두 번 쓰는 것

# print(rank1.find_next_siblings("li"))


webtoon = soup.find("a", text="독립일기")
print(webtoon)
