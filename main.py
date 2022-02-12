import requests
from bs4 import BeautifulSoup

page = requests.get("https://t.me/s/ProxyMTProto")


soup = BeautifulSoup(page.text, "html.parser")

with open('../soup.txt', 'w') as f:
    f.write(soup.text)
b = soup.find_all("code")
for item in b:
    print(item.text)
print(b[-1].text)