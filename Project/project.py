import re
import requests
from bs4 import BeautifulSoup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8%EC%A0%95%EB%B3%B4&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hOpAQdp0J1ZssBT59dGsssssthd-483264"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    cast = soup.find("p", {"class": "summary"}).get_text().strip()

    current_temp = soup.find(
        "div", attrs={"class": "temperature_text"}).get_text().strip()
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text()

    summary = soup.find(
        "dl", attrs={"class": "summary_list"}).get_text().strip()

    print(cast)
    print("{} ({}, {})".format(current_temp, min_temp, max_temp))
    print(summary)
    print()
    print()


def scarpe_news():
    print("[다음 헤드라인 뉴스]")
    url = "https://news.daum.net/"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    news_list = soup.find("div", attrs={"class": "pop_news pop_cmt"}).find(
        "ol", attrs={"class": "list_popcmt"}).find_all("li")

    for idx, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print(title, link)
        print()
        print()


def scrape_eng():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})

    print("(지문)")
    for sentence in sentences[:len(sentences)]:
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather()
    scarpe_news()
    scrape_eng()
