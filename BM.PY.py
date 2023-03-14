import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
# https://habr.com/ru/post/250975/
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

def get_source_html1(url):
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

def get_source_html(url):
    driver = webdriver.Chrome(
        #executable_path="driver_path"
    )

    #driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
        with open("page.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as _ex:
        print(_ex)
    #finally:
        #driver.close()
        #driver.quit()


def main():
    get_source_html(
        url="https://g1.botva.ru/")

    #get_source_html(
    #    url="https://g1.botva.ru/clan_members.php?id=21148")


if __name__ == "__main__":
    main()