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
import random
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
import mysettings
import traceback
from selenium.webdriver.firefox.options import Options
from selenium_stealth import stealth
'''
---------------------------------------------------------------------------'''


def main():
    print("[INFO] Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать билетики")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    mypf = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUMF"
    try:
        os.mkdir(mypf)
    except:
        print("Путь профиля лисы уже существует")
    print("Путь профиля Chrome: " + myp)
    print("Путь профиля FireFox: " + mypf)

    if 'drv' in locals():
        print('Движок определен')
    else:
        print('Движок не указан, пробуем Хром')
        drv = "C"

    if (drv=="F"):
        options = Options()
        options.add_argument('-profile')
        options.add_argument(mypf)
        driver = webdriver.Firefox(options=options)

    if (drv == "C"):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        '''
        options = webdriver.ChromeOptions()
        options.add_argument("--allow-profiles-outside-user-dir")
        options.add_argument(r"user-data-dir=" + myp)
        options.add_argument("--profile-directory=BOTVA")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        '''

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
    sleep(random.random() * 3)
    driver.get("https://g1.botva.ru/mine.php")
    sleep(2)
    mp = 0
    bp = 0
    try:
        elements = driver.find_elements(By.CLASS_NAME, "mt4")
        mp = elements[0].text
        #print(mp)
        bp = elements[1].text
        #print(bp)
        print(f' Билетов на малую поляну:   {mp}')
        print(f' Билетов на большую поляну: {bp}')
        bn = int(bp)
        mn = int(mp)
    except:
        print("Ошибка выбора количества билетов")
    try:
        t = driver.find_elements(By.CLASS_NAME, "cmd_arow5")
        t[1].click()
        sleep(random.random() * 2 + 3)
        for i in range(bn+1):
            print(f'Копаю большую - {i+1} / {bp}')
            t = driver.find_elements(By.CLASS_NAME, "cmd_arow4")
            t[1].click()
            sleep(random.random() * 2 + 2)
            # cmd_arow3 пропробовать ещё
            t = driver.find_element(By.CLASS_NAME, "cmd_arow3")
            t.click()
            sleep(random.random() * 3 + 2)
    except:
        print('Поймана ошибка при копке больших полян\n', "traceback.format_exc()")
    driver.get("https://g1.botva.ru/mine.php")
    try:
        t = driver.find_elements(By.CLASS_NAME, "cmd_arow5")
        t[0].click()
        sleep(random.random() * 2 + 3)
        for i in range(mn + 1):
            print(f'Копаю малую - {i + 1} / {mp}')
            t = driver.find_elements(By.CLASS_NAME, "cmd_arow4")
            t[1].click()
            sleep(random.random() * 2 + 2)
            # cmd_arow3 пропробовать ещё
            #t = driver.find_element(By.XPATH, "//a[contains(text(),'ВСЛЕПУЮ')]")
            t = driver.find_element(By.CLASS_NAME, "cmd_arow3")
            t.click()
            sleep(random.random() * 3 + 2)
    except:
        print('Поймана ошибка при копке малых полян\n', "traceback.format_exc()")
    driver.close()
if __name__ == "__main__":
    main()
