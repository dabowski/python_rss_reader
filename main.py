import colorama
import feedparser
from colorama import Fore, Style


def save_lines_to_array(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines


def save_line_to_file(line):
    with open('cache.txt', 'a') as f:
        f.write(line)
        f.write('\n')


def print_feed(feed, cache_array):
    print(Fore.RED, feed['channel']['title'], Style.RESET_ALL, '\n')
    for item in feed['items']:
        title_url = Fore.YELLOW + Style.BRIGHT + item['title'] + Style.RESET_ALL + item['link']
        # TODO bug-fix so that program do not print element that are in the cache.txt
        if title_url not in cache_array:
            print(title_url)
            save_line_to_file(title_url)
        else:
            pass


def print_feeds(url_array, cache_array):
    for url in url_array:
        print_feed(feedparser.parse(url), cache_array)
        print("Press any key to move to continue...")


if __name__ == "__main__":
    colorama.init()
    cache = save_lines_to_array("cache.txt")
    urls = save_lines_to_array("urls.txt")

    print_feeds(urls, cache)
