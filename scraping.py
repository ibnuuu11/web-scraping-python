import pandas as pd
import requests
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


# Header agar request lebih mirip browser
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def demo_1_requests():
    url = "https://www.detik.com/"
    res = requests.get(url, headers=HEADERS)

    print(res.status_code)
    print(res.content[:500])


def demo_2_urlopen():
    url = "https://www.detik.com/"

    req = Request(url, headers=HEADERS)

    html = urlopen(req)
    content = html.read()

    print(content[:500])


def demo_3_title():
    url = "https://www.detik.com/"

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title

    print(title)


def demo_4_find():
    url = "https://www.detik.com/"

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")

    print(title)


def demo_5_find_class():
    url = "https://www.detik.com/"

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")

    if title:
        print(title.get_text(strip=True))
    else:
        print("Tag h1 tidak ditemukan")


def demo_6_find_all():
    url = "https://www.detik.com/"

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("h1")

    for item in titles:
        print(item.get_text(strip=True))


def demo_7_csv():
    url = "https://www.detik.com/"

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    # Mengambil semua heading h2
    titles = soup.find_all("h2")

    data = []

    for item in titles:
        text = item.get_text(strip=True)

        if text:
            data.append(text)

    print(data)

    df = pd.DataFrame(data, columns=["title"])

    df.to_csv("detik.csv", index=False)

    print("Data berhasil disimpan ke detik.csv")


def demo_8_parser():
    url = "https://www.detik.com/"

    # Parser html.parser
    req = Request(url, headers=HEADERS)
    html = urlopen(req)

    soup1 = BeautifulSoup(html.read(), "html.parser")

    print("Dengan html.parser:")
    print(soup1.title)

    # Parser lxml
    req = Request(url, headers=HEADERS)
    html = urlopen(req)

    soup2 = BeautifulSoup(html.read(), "lxml")

    print("Dengan lxml:")
    print(soup2.title)


def demo_9_exception():
    # URL sengaja dibuat salah untuk menguji exception
    url = "https://www.detik.com/website-tidak-ada-123456"

    try:
        html = urlopen(url)

    except HTTPError as e:
        print("HTTP Error:", e)

    except URLError as e:
        print("The server could not be found!")

    else:
        print("It Worked!")


def getTitle(url):
    try:
        req = Request(url, headers=HEADERS)
        html = urlopen(req)

    except HTTPError as e:
        return None

    except URLError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), "html.parser")

        title = bs.title

    except AttributeError:
        return None

    return title


def demo_10_gettitle():
    title = getTitle("https://www.detik.com/")

    if title is None:
        print("Title could not be found")

    else:
        print(title.get_text(strip=True))


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
    jalankan("3. soup.title - Detik.com", demo_3_title)
    jalankan("4. soup.find('h1') - Detik.com", demo_4_find)
    jalankan("5. find dengan class", demo_5_find_class)
    jalankan("6. find_all dengan loop", demo_6_find_all)
    jalankan("7. Scraping to CSV - Detik.com", demo_7_csv)
    jalankan("8. Parser html.parser vs lxml", demo_8_parser)
    jalankan("9. Exceptions", demo_9_exception)
    jalankan("10. getTitle - Detik.com", demo_10_gettitle)