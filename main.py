from bs4 import BeautifulSoup
import lxml
import smtplib
import requests
from datetime import datetime, timedelta
from threading import Timer

URL = "https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=lp_16225007011_1_3"
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

response = requests.get(url=URL, headers=headers)
amazon = response.text
soup = BeautifulSoup(amazon, "lxml")
print(soup)
price = soup.find_all(name="span", class_="a-offscreen")
num = 0
digit = None
for x in price:
    if num == 0:
        num += 1
        digit = float(x.getText().split("$")[1])
        print(digit)


def alert_deal():
    if digit < 150:
        MY_EMAIL = "wangsolong86@gmail.com"
        PASSWORD = "childofgod1"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="shakayahaya4@gmail.com",
                                msg=f"Subject:DEAL!\n\nItem price now is {digit}\n{URL}")


x = datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t = y - x

secs = delta_t.total_seconds()

t = Timer(secs, alert_deal())
t.start()
