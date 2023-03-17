#mmtype

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
    sleep(random.random() * 2)

    #driver.refresh()


    #driver.get("https://g1.botva.ru/mine.php")
    #element = driver.find_element(By.NAME, "mmtype")
    driver.get("https://g1.botva.ru/monster.php?a = monsterpve")
    t = ""
    while t != 'Пристанище 5-го уровня':
        print(f'T = {t}')
        try:
            element = driver.find_element(By.NAME, "mmtype")
            t = element.text
            if t == 'Пристанище 5-го уровня':

                element = driver.find_element(By.NAME, "mmtype")
                element.click()
                print(element.text)
        except:
            print(element.text)
        sleep(10)
        driver.refresh()
        element = driver.find_element(By.NAME, "mmtype")






if __name__ == "__main__":
    main()
