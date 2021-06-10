import colorama
import feedparser
from colorama import Fore, Style


def save_lines_to_array(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines


def print_feed(feed):
    print(Fore.RED, feed['channel']['title'], Style.RESET_ALL, '\n')
    for item in feed['items']:
        title_url = Fore.YELLOW + Style.BRIGHT + item['title'] + Style.RESET_ALL + " " + item['link']
        print(title_url)


def print_feeds(url_array):
    for url in url_array:
        print_feed(feedparser.parse(url))
        print("Press any key to move to continue...")


if __name__ == "__main__":
    colorama.init()
    urls = save_lines_to_array("urls.txt")

    print_feeds(urls)
