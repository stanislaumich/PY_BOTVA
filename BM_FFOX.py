'''
Есть
список воинов клана на дату
походы в подзем на дату и номер с лотереей

 -- казна на дату - совместима с ботвой дельфи и проверена
 -- выполнение КЗ - совместимо с ботвой

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
from bs4 import BeautifulSoup
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
    #print(base)
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
    #sys.exit()

    #driver = webdriver.Chrome()
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
    '''
    driver.get("https://g1.botva.ru/clan_members.php?id=21148")
    sleep(3)
    #now = date.today()
    #ds = str(now.day)+"." + str(now.month)+"." + str(now.year)
    #with open(dt+"_"+tm+"_KLAN.html", "w", encoding="utf-8") as file:
    #    file.write(driver.page_source)
    print("Обработка БМ")
    fl = []
    elements = driver.find_elements("xpath", '//tr[contains(@class, "row_")]')
    for el in elements:
        nik = el.find_element(By.CLASS_NAME, "profile ").text
        print(nik)
        bm = el.find_element(By.CLASS_NAME, "right").text
        print(bm)
        sl = el.find_element(By.CLASS_NAME, "nowrapi").text
        print(sl)
        zv = el.find_element(By.CLASS_NAME, "pl5").text
        print(zv)
        bob = (nik, bm, sl, dt, tm, zv)
        fl.append(bob)
    cursor.executemany("INSERT INTO KLAN (nik, bm, sl, dt, tm, dop) VALUES (?, ?, ?, ?, ?, ?)", fl)
    con.commit()

    # пробуем работать со списком походов в подзем
    print("Обработка подзема")
    f1 = open('podzem.txt')
    flist = f1.readlines()
    for el in flist:
        crt = el.split('\t')
        print(crt[0])
        # вот это для каждой строки
        dt = crt[0]
        for i in range(1, 3):
            # первая и вторая ссылки в строке
            href = crt[i]
            #href = "https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=903197&id=2648065&key=de67129a78b6b4fe08e4e69fbfa09eb3"
            idp0 = href.split("&")
            idp1 = idp0[3].split("=")
            idp = idp1[1]
            driver.get(href)
            sleep(10)
            master = driver.find_element(By.CLASS_NAME, "profile ").text
            print(f"Master: {master}")
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            bob = (dt, i, master, -1)
            cursor.execute(sql_select_query, bob)
            con.commit()
            elements = driver.find_elements(By.CLASS_NAME, "round3")
            cnt = 0
            bl = []
            for elz in elements:
                cnt = cnt + 1
                ts = elz.text
                ts = ts.replace("...", "%")
                sql_select_query = """select nik from klan where nik like ?"""
                cursor.execute(sql_select_query, (ts,))
                record = cursor.fetchone()
                ts = record[0]
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
    '''
    '''
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
    '''
    # ОБРАБОТКА КЛАНОВОГО ЗАДАНИЯ
    print("Обработка кланового задания")
    driver.get("https://g1.botva.ru/clan_mod.php?m=task")
    '''
    zd = driver.find_elements(By.CLASS_NAME, "mb5")
    zdn = zd[1].text
    print("Задание: " + zdn)
    '''
    html = driver.page_source
    sleep(2)
    flz = []
    bs = BeautifulSoup(html, "lxml")
    tb = bs.find(class_="default profile_statistic")
    tr = tb.find_all("tr")
    for e in tr:
        tnik = e.find(class_="borderr").find("a")
        try:
            nik = tnik.text
        except:
            nik = ""
        finally:
            nik = nik
        plr = e.find(class_="center")
        try:
            pl = plr.text
        except:
            pl = ""
        finally:
            pl = pl
        if nik != "":
            bob = (dt, 1, nik, pl)
            flz.append(bob)
        print(nik)
        print(pl)
    cursor.executemany("INSERT INTO zad (dt,tip,nik,val)VALUES(?,?,?,?)", flz)
    con.commit()





# all_cookies = driver.get_cookies()
# for cookie_name, cookie_value in all_cookies:
#    print("%s : %s", cookie_name, cookie_value)

if __name__ == "__main__":
    main()

