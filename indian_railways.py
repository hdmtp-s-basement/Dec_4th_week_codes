import requests
from bs4 import BeautifulSoup

n = int(input("Enter any integer (Max Limit: 363459): "))
url = f"https://indiarailinfo.com/blog/{n}?tp=1"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

content = soup.prettify()

print(soup.title.string)


count = 0
l=[]
for i in soup.find_all('a', attrs = {"style":"font-weight:bold;"}):
    if str(i.text) != "General Travel":
        count += 1
        l.append(i.text)

for i in range(1, count):
    print(f"{l[i]}\n")

print(count)