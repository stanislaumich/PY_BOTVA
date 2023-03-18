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

#drv = "E"
tm = 5 # таймаут обновления страницы ускора в секндах
def main():
    print("[INFO] Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать билетики")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    try:
        os.mkdir(myp)
    except:
        print("Путь профиля хром уже существует")
    mypf = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUMF"
    try:
        os.mkdir(mypf)
    except:
        print("Путь профиля лисы уже существует")
    print("Путь профиля Chrome: " + myp)
    print("Путь профиля FireFox: " + mypf)

    if mysettings.drv == "F":
        print("Движок Firefox")
        options = Options()
        options.add_argument('-profile')
        options.add_argument(mypf)
        driver = webdriver.Firefox(options=options)

    if mysettings.drv == "C":
        print("Движок Chrome")
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

    if (mysettings.drv =="E"):
        print("Движок Edge")
        #options = Options()
        #options.add_argument('-profile')
        #options.add_argument(mypf)
        driver = webdriver.Edge()

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
    #sleep(100)
    element = driver.find_element("name", "server")
    element.send_keys("t")
    #element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element = driver.find_element(By.XPATH, '//*[@id="auth_form_email"]/form/div[4]/div/input')
    #sleep(1000)
    element.submit()
    #sleep(1000)
    sleep(random.random() * 2 + 0.5)
    #driver.refresh()
    #driver.get("https://g1.botva.ru/mine.php")
    #element = driver.find_element(By.NAME, "mmtype")
    driver.get("https://g1.botva.ru/monster.php?a=monsterpve")
    # /html/body/div[5]/div[3]/div[2]/div[2]/div[2]/div[4]/form/input[3]
    # вот этот путь существует если есть ускор и его надо кликнуть
    t = True
    while t:
        try:
            element = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div[2]/div[2]/div[4]/form/input[3]")
            t = element.click()
            print("УРАА!!")
            #if t == 'ПЕРЕЙТИ К МЕСТУ СБОРА ОТРЯДА':
            #    element.click()
            #    print(element.text)
            #    t = False
        except:
            print("Не найдено")
        sleep(tm)
        driver.get("https://g1.botva.ru/monster.php?a=monsterpve")







if __name__ == "__main__":
    main()
