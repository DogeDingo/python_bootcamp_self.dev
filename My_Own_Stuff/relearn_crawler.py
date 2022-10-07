import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin #>> fuer zusammenfuegen von Links (verwendet fuer image links)
import time
import csv

url = "http://python.beispiel.programmierenlernen.io/index.php"

class CrawledArticle():
    def __init__(self, headline, emoji, content, image):
        self.headline = headline
        self.emoji = emoji
        self.content = content
        self.image = image

class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        checker = True
        while checker == True:
            time.sleep(3)
            print(url)
            crawled_url = requests.get(url)
            html_document = BeautifulSoup(crawled_url.text, "html.parser")
            testing_unit = html_document.select_one(".navigation a")
            if testing_unit is None:
                for element in html_document.select(".card"):
                    emoji = element.select(".emoji")[0].text
                    headline = element.select(".card-title span")[1].text
                    # man liest von rechts nach links daher span zuerst und dann erst die Klasse
                    content = element.select_one(".card-text").text
                    image = urljoin(url, element.select_one("img").attrs["src"])

                    yield CrawledArticle(headline, emoji, content, image)
                checker = False
            else:
                href_class = html_document.select_one(".navigation a").attrs["href"]
                #select() function from Beautifulsoup
                for element in html_document.select(".card"):
                    emoji = element.select(".emoji")[0].text
                    headline = element.select(".card-title span")[1].text
                    # man liest von rechts nach links daher span zuerst und dann erst die Klasse
                    content = element.select_one(".card-text").text
                    image = urljoin(url, element.select_one("img").attrs["src"])

                    yield CrawledArticle(headline, emoji, content, image)
                url = urljoin(url, href_class)

fetcher = ArticleFetcher()

counter = 0
for article in fetcher.fetch():
    if counter == 40:
        break
    counter = counter + +1
    print(article.emoji + ": " + article.headline)

# with open('crawler_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     for article in fetcher.fetch():
#         articlewriter.writerow([article.emoji, article.headline, article.image, article.content])

#Link immer neu generieren lassen
# if-else statement nutzen um zu ueberpruefen ob letzte seite oder nicht
# auf den Button Zur Naechsten Seite zugreifen koennen


