'''
Список воинов клана их БМ и слава

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
import pickle

def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает обработать казну")
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("s:\\config.ini")  # читаем конфиг
    basepath = config["PATH"]["workdir"]
    try:
        os.mkdir(basepath)
    except:
        print("Проверка рабочей папки")
    finally:
        print(" ")
    base = config["PATH"]["base"]
    print("Создаем и открываем базу данных: "+base)
    con = sqlite3.connect(base)
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS VOIN (id BIGINT, nik VARCHAR(50) DEFAULT NULL, 
    url VARCHAR(5000) DEFAULT NULL, BM BIGINT, SLAVA BIGINT, Lev INTEGER,    
    dt VARCHAR(50) DEFAULT NULL, tm VARCHAR(50))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS podzem (dt VARCHAR (50), num INTEGER, nik VARCHAR2 (50), 
    id  INTEGER, val VARCHAR2 (1000))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS kazna (dt VARCHAR(30), nik VARCHAR(100), gold VARCHAR(30),
    pirah VARCHAR(30), kri VARCHAR(30))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS zad(id INTEGER PRIMARY KEY AUTOINCREMENT, dt VARCHAR(30),
    tip INTEGER, nik VARCHAR(300), val INTEGER)""")

    nw = datetime.now()
    dt = nw.strftime("%d.%m.%Y")
    tm = nw.strftime("%I-%M")
    print("База данных - Ok")
    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: "+myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir="+myp)
    options.add_argument("--profile-directory=BOTVA")
    driver = webdriver.Chrome(options=options)
    print("Логин...  ")

    try:
        for cookie in pickle.load(open("QuoraCookies.pkl", "rb")):
            driver.add_cookie(cookie)
            print(cookie)
    except:
        sleep(1)
    finally:
        sleep(1)
    driver.get("http://botva.ru")
    sleep(5)
    try:
        element = driver.find_element(By.CLASS_NAME, "sign_in")
        element.click()
        element = driver.find_element("name", "email")
        element.send_keys(config["LOGIN"]["username"])
        element = driver.find_element("name", "password")
        element.send_keys(config["LOGIN"]["password"])
        element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
        element.submit()
    except:
        sleep(1)
    finally:
        sleep(3)

    pickle.dump(driver.get_cookies(), open("QuoraCookies.pkl", "wb"))
    driver.get("https://g1.botva.ru/clan_members.php?id=21148")

    sleep(3)
    print("Обработка БМ")
    fl = []
    elements = driver.find_elements("xpath", '//tr[contains(@class, "row_")]')
    for el in elements:
        nik = el.find_element(By.CLASS_NAME, "profile ").text
        print(nik)
        bm = el.find_element(By.CLASS_NAME, "right").text
        bm = bm.replace(".", "")
        print(bm)
        sl = el.find_element(By.CLASS_NAME, "nowrapi").text
        sl = sl.replace(".", "")
        print(sl)
        zv = el.find_element(By.CLASS_NAME, "pl5").text
        print(zv)
        bob = (nik, bm, sl, dt, tm)
        fl.append(bob)
    cursor.executemany("INSERT INTO KLAN (nik, bm, sl, dt, tm) VALUES (?, ?, ?, ?, ?)", fl)

    ''' nik, url,BM, SLAVA, Lev, dt, tm'''

    con.commit()

if __name__ == "__main__":
    main()
