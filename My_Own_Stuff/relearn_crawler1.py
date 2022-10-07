import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://python.beispiel.programmierenlernen.io/index.php"
crawled_url = requests.get(url)
html_document = BeautifulSoup(crawled_url.text, 'html.parser')


next_button = html_document.select_one(".navigation")
href_class = html_document.select_one(".navigation a").attrs["href"]
print(next_button)
print(href_class)

if "index.php" in href_class:
    print("hat geklappt")
else:
    print("hat es nicht")
# new_link = urljoin(url, href_class)
# print(new_link)

checker = True
x = 0
while checker == True:
    if x < 5:
        print(x)
        x += 1
    else:
        checker = False

