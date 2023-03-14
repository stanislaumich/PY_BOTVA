'''
Обработка подземов по файлу списка каждая строка - дата и 2 ссылки через пробел
15.02.2023	https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=907729&id=2664712&key=e4dc1a7fd8a645981be1ffeba219f59b	https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=907765&id=2664821&key=ebe2a0b5f876246c78a1e39140a530a3

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver


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
    cursor.execute("""CREATE TABLE IF NOT EXISTS podzemurl (dt VARCHAR (50), 
    url1  VARCHAR (1000), url2 VARCHAR (1000))""")

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
    # пробуем работать со списком походов в подзем
    print("Обработка подзема")
    f1 = open('podzem.txt')
    flist = f1.readlines()
    gurl = []
    gdt = ""
    url = []
    for el in flist:
        crt = el.split('\t')
        print(crt[0])
        dt = crt[0]

        for i in range(1, 3):
            # первая и вторая ссылки в строке
            href = crt[i]
            print(href)
            #url[i] = href
            idp0 = href.split("&")
            idp1 = idp0[3].split("=")
            idp = idp1[1]
            driver.get(href)
            sleep(10)
            master = driver.find_element(By.CLASS_NAME, "profile ").text
            print(f"Master: {master}")
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            bob = (dt, i, master, -1)
            gdt = dt
            cursor.execute(sql_select_query, bob)
            con.commit()
            elements = driver.find_elements(By.CLASS_NAME, "round3")
            cnt = 0
            bl = []
            for elz in elements:
                cnt = cnt + 1
                ts = elz.text
                print(ts)
                ts = ts.replace("...", "%")
                sql_select_query = """select nik from voin where nik like ?"""
                cursor.execute(sql_select_query, (ts,))
                record = cursor.fetchone()
                ts = record[0].upper()
                print(ts)
                bob = (dt, i, ts, cnt)
                bl.append(bob)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            cursor.executemany(sql_select_query, bl)
            con.commit()
            on = (dt, i, "", -2, href)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            cursor.execute(sql_select_query, on)
            con.commit()
            loter = int(idp) % cnt
            if loter == 0:
                loter = cnt
            pts = idp + f" mod {cnt} = " + str(loter)
            on = (i, dt, loter)
            sql_select_query = """select nik from podzem where num = ? and dt = ? and id = ?"""
            cursor.execute(sql_select_query, on)
            pobed1 = cursor.fetchone()
            pobed = pobed1[0]
            on = (dt, i, pobed, -3, pts)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            cursor.execute(sql_select_query, on)
            con.commit()

        #gbob = (gdt, url[1], url[2])
        #gurl.append(gbob)

    #cursor_q = "insert into podzemurl (dt, url1, url2) values(?,?,?)"
    #cursor.executemany(cursor_q, gbob)


if __name__ == "__main__":
    main()
