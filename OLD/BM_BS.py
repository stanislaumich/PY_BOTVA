"""
https://g1.botva.ru/clan_members.php?id=31481

для этого скрипта нужно доинсталлить вот эти
pip install bs4 lxml requests



# ищет все теги с CSS классом, в именах которых встречается "itl"
soup.find_all(class_=re.compile("itl"))


"""
import time
from bs4 import BeautifulSoup
import requests
# import lxml
# import re

# url = 'https://g1.botva.ru/clan_members.php?id=31481'  # Авалоны
# url = 'https://g1.botva.ru/clan_members.php?id=55626'  # Мисты
url = 'https://g1.botva.ru/clan_members.php?id=21148'  # Мы

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value

#print remove(filename, '\/:*?"<>|')

def main():
    print("[INFO] ")
    page = requests.get(url)
    print(page.status_code)
    html = page.content
    soup = BeautifulSoup(html, "lxml")


    el = soup.find('a', class_='profile')
    klan = el.text

    tm = time.localtime(time.time())
    fname = "{}.{}.{}.{}.{}.{}".format(tm.tm_mday, tm.tm_mon, tm.tm_year, tm.tm_hour, tm.tm_min, tm.tm_sec)
    fname = fname + ".csv"
    fname = remove(klan + '_' + fname, '\/:*?"<>|')

    f = open('BM___' + fname, 'w')
    ff = open('FULL_' + fname, 'w')

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
    # print(all_cols)
    f.write(f'{klan};{url}\n')
    ff.write(f'{klan};{url}\n')
    for r in all_cols:
        f.write(f"{r[0]};{r[2]}\n")
        ff.write(f"{r[0]};{r[2]};{r[3]};{r[4]}\n")
    f.close()
    ff.close()
    print('Обработка завершена, проверьте файл с сегодняшней датой')


if __name__ == "__main__":
    main()
