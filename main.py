import colorama
import feedparser
from colorama import Fore, Style


def save_urls(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines


def print_feed(feed):
    print(Fore.RED, feed['channel']['title'], Style.RESET_ALL, '\n')
    for item in feed['items']:
        print(Fore.YELLOW, Style.BRIGHT, item['title'], Style.RESET_ALL, item['link'], "\n")


colorama.init()
for url in save_urls('urls.txt'):
    print_feed(feedparser.parse(url))
    input("Press any key to move forward...")
