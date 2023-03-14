'''
Программа для открытия билетов
в командной строке нужно выполнить только первый раз, больше не надо
pip install selenium
для установки средств управления браузером
в файле 
mysettings.py прописать логин и пароль для входа в ботву
и положить его рядом с этим скриптом

Установленный питон, версия любая в принципе но на винде 7 и ниже могут быть сложности

Скрипт лучше всего положить в отдельную папку на диске, не на рабочем столе

При работе - откроется черное окно, откроется браузер,
залогинится и начнет открывать билеты, затем закроется
во время работы можно окна свернуть и заниматься своими делами

При работе в папке скрипта создастся папка SELENIUM - это кэш браузера
иногда бывает глюк - скрипт падает с ошибкой, можно папку удалить
скрипт её пересоздаст



'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
import mysettings

'''
Ниже идут настройки 
'''
BN = 100
MN = 100

'''
---------------------------------------------------------------------------'''


def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать прокачку")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: " + myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir=" + myp)
    options.add_argument("--profile-directory=BOTVA")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    print("Логин...  ")

    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    # element.send_keys(config["LOGIN"]["username"])
    element.send_keys(mysettings.login)
    element = driver.find_element("name", "password")
    # element.send_keys(config["LOGIN"]["password"])
    element.send_keys(mysettings.passw)
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
    driver.get("https://g1.botva.ru/mine.php")
    # class="mt4"
    elements = driver.find_elements(By.CLASS_NAME, "mt4")
    mp = elements[0].text
    bp = elements[1].text
    print(f' Билетов на малую поляну:   {mp}')
    print(f' Билетов на большую поляну: {bp}')
    bn = int(bp)
    mn = int(mp)

    t = driver.find_elements(By.CLASS_NAME, "cmd_arow5")
    t[1].click()
    sleep(1)
    for i in range(4):
        print(i)
        t = driver.find_elements(By.CLASS_NAME, "cmd_arow4")
        t[1].click()
        sleep(2)
    driver.get("https://g1.botva.ru/mine.php")
    # driver.find_element_by_link_text("МАЛЕНЬКАЯ").click()


if __name__ == "__main__":
    main()
