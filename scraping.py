import pandas as pd
import requests 
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def demo_1_requests():
    res = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
    print(res.status_code)
    print(res.content[:500])  # dipotong 500 karakter supaya tidak terlalu panjang


def demo_2_urlopen():
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    content = html.read()
    print(content)


def demo_3_title():
    url = "https://unm.ac.id/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title
    print(title)

def demo_4_find():
    url = "https://chomsky.info/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('h1')
    print(title)


def demo_5_find_class():
    url = "https://chomsky.info/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("div", class_="header_nav_el_mobile")
    print(title.get_text(strip=True))


def demo_6_find_all():
    url = "https://chomsky.info/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find_all("div", class_="header_nav_el_mobile")

    for item in title:
        print(item.get_text(strip=True))



def demo_7_csv():
    url = "https://chomsky.info/audionvideo/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("li")

    data = []

    for item in titles:
        data.append(item.get_text(strip=True))

    print(data)

    df = pd.DataFrame(data, columns=["title"])
    df.to_csv("chomsky.csv", index=False)



def demo_8_parser():
    # Pakai parser bawaan
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    soup1 = BeautifulSoup(html.read(), "html.parser")
    print("Dengan html.parser:", soup1.h1.get_text())

    # Pakai parser lxml
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    soup2 = BeautifulSoup(html.read(), "lxml")
    print("Dengan lxml:", soup2.h1.get_text())

def demo_9_exception():
    try:
        html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
    except HTTPError as e:
        print("HTTP Error:", e)
    except URLError as e:
        print("The server could not be found!")
    else:
        print("It Worked!")

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


def demo_10_gettitle():
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title is None:
        print('Title could not be found')
    else:
        print(title.get_text())

def jalankan(nama, fungsi):
    print("\n" + "=" * 60)
    print(nama)
    print("=" * 60)
    try:
        fungsi()
    except Exception as e:
        print("Terjadi error:", e)


if __name__ == "__main__":
    jalankan("1. Requests Module", demo_1_requests)
    jalankan("2. urlopen", demo_2_urlopen)
    jalankan("3. soup.title (URL sudah diubah)", demo_3_title)
    jalankan("4. soup.find('h1')", demo_4_find)
    jalankan("5. find dengan class", demo_5_find_class)
    jalankan("6. find_all dengan loop", demo_6_find_all)
    jalankan("7. Scraping to CSV", demo_7_csv)
    jalankan("8. Parser html.parser vs lxml", demo_8_parser)
    jalankan("9. Exceptions", demo_9_exception)
    jalankan("10. getTitle", demo_10_gettitle)