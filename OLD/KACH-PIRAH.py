'''
Программа для прокача ботвы пирахами
в командной строке нужно выполнить только первый раз, больше не надо
pip install selenium configparser
для установки средств управления браузером
в файле mysettings.py прописать логин и пароль для входа в ботву
и положить его рядом с этим скриптом

Установленный питон, версия любая в принципе но на винде 7 и ниже могут быть сложности

Скрипт лучше всего положить в отдельную папку на диске, не на рабочем столе

При работе - откроется черное окно, откроется браузер,
залогинится и начнет качать, затем закроется
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
N = 50 # Сколько раз выполнять операцию прокачки
V1 = "1" # Сила                        сколько статов качнуть за 1 раз, от 0 до 99999, у меня 1  для теста
V2 = "1" # Защита
V3 = "0" # Ловкость       # у меня ловкость максималка поэтому 0, если на макс поставить хоть 1 не даст качать ничего
V4 = "1" # Масса
V5 = "1" # Мастерство                  любая комбинация статов от 0 до 99999

pause = 5 # это настройка паузы, если компьютер не успевает обсчитать статы надо увеличивать

'''---------------------------------------------------------------------------'''
def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать прокачку")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: " + myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir=" + myp)
    options.add_argument("--profile-directory=BOTVA")
    driver = webdriver.Chrome(chrome_options=options)
    print("Логин...  ")

    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    #element.send_keys(config["LOGIN"]["username"])
    element.send_keys(mysettings.login)
    element = driver.find_element("name", "password")
    #element.send_keys(config["LOGIN"]["password"])
    element.send_keys(mysettings.passw)
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
    # залогинились и подождали 3 секунды ищем кнопку кача
    element1 = driver.find_element(By.CLASS_NAME, "mr-20")
    element1.click()
    sleep(1)
    element2 = driver.find_element(By.CLASS_NAME, "training_tab_2")
    element2.click()
    sleep(1)
    for i in range(N):
        # сила - power, защита - block, ловкость - dexterity, масса - endurance, мастерство - charisma
        element3 = driver.find_element(By.XPATH, "//input[@id='power']")
        element3.clear()
        element3.send_keys(V1)
        element3 = driver.find_element(By.XPATH, "//input[@id='block']")
        element3.clear()
        element3.send_keys(V2)
        element3 = driver.find_element(By.XPATH, "//input[@id='dexterity']")
        element3.clear()
        element3.send_keys(V3)
        element3 = driver.find_element(By.XPATH, "//input[@id='endurance']")
        element3.clear()
        element3.send_keys(V4)
        element3 = driver.find_element(By.XPATH, "//input[@id='charisma']")
        element3.clear()
        element3.send_keys(V5)
        sleep(pause)
        element4 = driver.find_element(By.XPATH, "//input[@id='btn_fish']")
        element4.click()
        sleep(2)


if __name__ == "__main__":
    main()