'''
Обработка подземов по файлу списка каждая строка - дата и 2 ссылки через пробел
15.02.2023	https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=907729&id=2664712&key=e4dc1a7fd8a645981be1ffeba219f59b	https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=907765&id=2664821&key=ebe2a0b5f876246c78a1e39140a530a3

'''
import sys
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import sqlite3
from selenium import webdriver
import mysettings
from bs4 import BeautifulSoup
import requests

base = "31.10.2023"
url = 'https://g1.botva.ru/clan_members.php?id=21148'  # Мы

myklan = []

def form_voin_list():

    con = sqlite3.connect(base+".SQLITE")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS VOIN
                        (nik TEXT, pohod integer, lid integer)""")
    cursor.execute("delete from VOIN where 1=1")
    con.commit()
    page = requests.get(url)
    print(page.status_code)
    html = page.content
    soup = BeautifulSoup(html, "lxml")
    el = soup.find('a', class_='profile')
    klan = el.text
    fname = base + ".KLAN"
    ff = open(fname, 'w')
    print(klan)
    table = soup.find_all('table')
    all_cols = []
    for row in table:
        cols = row.find_all('td')
        rw = []
        i = 0
        for c in cols:
            c = c.text.replace('\n', '')
            c = c.replace('\r', '')
            c = c.replace('&nbsp', '')
            c = c.strip(' ')
            c = c.strip(chr(160))
            c = c.strip(' ')
            if c != '':
                rw.append(c)
                i = i + 1
                if i == 5:
                    i = 0
                    e = tuple(rw)
                    all_cols.append(e)
                    rw.clear()
    for r in all_cols:
        ff.write(f"{r[0]};{r[2]};{r[3]};{r[4]}\n")
        s = r[0].upper()
        klant = (r[0], r[2], r[3], r[4])
        myklan.append(klant)
        cursor.execute("INSERT INTO VOIN (nik, pohod, lid) VALUES ('"+s+"',0 ,0)")
        con.commit()
    ff.close()
    con.close()
    print(myklan)


def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает обработать казну")
    print("Вычитываем список воинов клана в файл")
    form_voin_list()
    print('Обработка воинов клана завершена')
    con = sqlite3.connect(base + ".SQLITE")
    #  sys.exit()

    fname = base + ".PODZEM"
    f = open(fname, 'w')
    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: "+myp)
    try:
        os.mkdir(myp)
    except:
        print("Путь профиля хром уже существует")

    #opts = uc.Options()
    #if os.path.exists('s:/home'):
    #    opts.add_argument(f'--proxy-server=127.0.0.1:3128')
    #opts.add_argument(r"--user-data-dir=" + myp)
    #opts.add_argument("--profile-directory=BOTVA")
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir=" + myp)
    options.add_argument("--profile-directory=BOTVA")

    driver = webdriver.Chrome(options=options,executable_path=r"c:\chromedriver\driver.exe")
    '''stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    '''
    print("Логин...  ")
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.clear()
    element.send_keys(mysettings.login)
    element = driver.find_element("name", "password")
    element.clear()
    element.send_keys(mysettings.passw)
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(1)

    # пробуем работать со списком походов в подзем
    print("Обработка подзема")
    f1 = open('podzem.txt')
    flist = f1.readlines()
    con = sqlite3.connect(base + ".SQLITE")
    cursor = con.cursor()
    lost = 0
    for el in flist:
        if el.startswith(('0', '1', '2', '3')):
            crt = el.split('\t')
            print(crt[0])
            dt = crt[0]

            for i in range(1, 3):
                # первая и вторая ссылки в строке
                href = crt[i]
                print(href)
                idp0 = href.split("&")
                idp1 = idp0[3].split("=")
                idp = idp1[1]
                driver.get(href)
                sleep(1)
                master = driver.find_element(By.CLASS_NAME, "profile ").text
                print(f"Master: {master}")
                ts = master.upper()
                ts = ts.replace("...", "%")
                sql_select_query = "select nik from voin where nik like '" + ts + "'"
                cursor.execute(sql_select_query)
                record = cursor.fetchone()

                try:
                    ts = record[0]
                    print(f"Found: {ts}")
                except:
                    lost = lost +1
                #  print(ts)
                cursor.execute("update VOIN set lid = lid+2 where nik = '" + ts + "'")
                con.commit()
                bob = dt+";" + str(i) + ";" + master + ";" + "2"+'\n'
                f.write(bob)

                elements = driver.find_elements(By.CLASS_NAME, "member")
                cnt = 0
                for elz in elements:
                    cnt = cnt + 1
                    ts = elz.text.upper()
                    #  print(ts)
                    ts = ts.replace("...", "%")
                    sql_select_query = """select nik from voin where nik like ?"""
                    cursor.execute(sql_select_query, (ts,))
                    record = cursor.fetchone()
                    try:
                        ts = record[0]
                    except:
                        pass
                    print(ts)
                    bob = dt + ";" + str(i) + ";" + ts + ";" + "1" + '\n'
                    cursor.execute("update VOIN set pohod = pohod+1 where nik = '" + ts + "'")
                    con.commit()
                    f.write(bob)

            #  sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            #  cursor.executemany(sql_select_query, bl)
            #  con.commit()
            #  on = (dt, i, "", -2, href)
            #  sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            #  cursor.execute(sql_select_query, on)
            #  con.commit()
            #  loter = int(idp) % cnt
            # if loter == 0:
            #      loter = cnt
            #  pts = idp + f" mod {cnt} = " + str(loter)
            #  on = (i, dt, loter)
            #  sql_select_query = """select nik from podzem where num = ? and dt = ? and id = ?"""
            #  cursor.execute(sql_select_query, on)
            #  pobed1 = cursor.fetchone()
            #  pobed = pobed1[0]
            #  on = (dt, i, pobed, -3, pts)
            #  sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            #  cursor.execute(sql_select_query, on)
            #  con.commit()

    f.close()
    """
    Сохраняем базу в текст
    """
    rfname = base + ".RESULT"
    rf = open(rfname, 'w')
    q = "select nik, sum(pohod) p, sum(lid) l from voin group by nik order by sum(pohod)+sum(lid) desc"
    cursor.execute(q)
    records = cursor.fetchall()
    for row in records:
        ts = row[0] + ";" +  str(row[1]) + ";" + str(row[2]) + ";\n"
        print(ts)
        rf.write(ts)
    con.close()
    rf.close()
    print(f"Утеряно мастеров : {lost}")


if __name__ == "__main__":
    main()
