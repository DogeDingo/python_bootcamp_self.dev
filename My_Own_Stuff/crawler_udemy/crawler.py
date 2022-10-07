import crawler

fetcher = crawler.ArticleFetcher()

counter = 0
for element in fetcher.fetch():
    if counter == 5:
        break
    counter += 1
    print(element.headline)