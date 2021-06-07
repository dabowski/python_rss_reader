import feedparser


def save_urls(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines


def print_feed(feed):
    print(feed['channel']['title'])
    for item in feed['items']:
        print(item['title'], item['link'], "\n")


for url in save_urls('urls.txt'):
    print_feed(feedparser.parse(url))
    input("Press any key to move forward...")
