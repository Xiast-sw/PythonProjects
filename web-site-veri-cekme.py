import requests
from bs4 import BeautifulSoup

#5 yillik altin fiyat verisini cekme
url = requests.get("https://www.altinpiyasa.com/arsiv")

if url.status_code ==200:
    print("siteden veri çekilebilir")
else:
    print("siteden veri çekilemez")

soup=BeautifulSoup(url.content,"html.parser")


for i in soup.find("tbody").find_all("tr"):
    print(i)
