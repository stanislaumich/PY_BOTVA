'''
Обрабротка казны клана

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver

''''''

def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает обработать казну")
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("config.ini")  # читаем конфиг
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
    cursor.execute("""CREATE TABLE IF NOT EXISTS KLAN
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    nik TEXT, 
                    bm  text,
                    sl  text,
                    dt  text,
                    tm  text,
                    dop text)""")
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
    driver = webdriver.Chrome(chrome_options=options)
    print("Логин...  ")
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys(config["LOGIN"]["username"])
    element = driver.find_element("name", "password")
    element.send_keys(config["LOGIN"]["password"])
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
# ОБРАБОТКА КАЗНЫ
    print("Обработка казны")
    driver.get("https://g1.botva.ru/clan_mod.php?m=treasury")
    # получим все строки таблицы
    flk = []
    r = driver.find_elements("xpath", "//table[@id='treasury_givements_table2']/tbody/tr")
    for s in r:
        t = s.text
        arr = t.split("\n")
        nik = arr[0]
        p = arr[1].split(" ")
        gold = p[0].replace(".", "")
        kri = p[1].replace(".", "")
        pirah = p[2].replace(".", "")
        print(nik)
        print(gold)
        print(kri)
        print(pirah)
        bob = (dt, nik, gold, pirah, kri)
        flk.append(bob)
    cursor.executemany("INSERT INTO kazna (dt,nik,gold,pirah,kri)VALUES (?,?,?,?,?)", flk)
    con.commit()


if __name__ == "__main__":
    main()
