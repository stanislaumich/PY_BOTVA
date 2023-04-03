import sys
from time import sleep
import os

from bs4 import BeautifulSoup
import requests

url = 'https://www.figma.com/community/tag/web/files/figma/free/popular'

def main():


    page = requests.get(url)
    print(page.status_code)
    html = page.content
    print(html)
    soup = BeautifulSoup(html, "lxml")
    #  el = soup.findAll('div' ,attrs = {'class' = 'feed_page--hubFile--W-gQT feed_page--resourceLinkTag--sQP8O'})
    el = soup.findAll('div', attrs={'class': 'feed_page--hubFile--W-gQT feed_page--resourceLinkTag--sQP8O'})
    print(el)


if __name__ == "__main__":
    main()