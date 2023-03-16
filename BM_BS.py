'''
https://g1.botva.ru/clan_members.php?id=31481


pip install bs4 lxml requests

<tr class="row_0">
<td data-sort-value="">
</td>
<td class="left pt3 pb3 pr3 borderr">
<b class="icon race21" title="Барантус"></b>
                                                 
                        <a class="profile" href="/player.php?id=5074120">=Rottweiler=</a>
</td>
<td class="p3 borderr center" data-sort-value="100">100</td>
<td class="p3 borderr right" data-sort-value="52398600999">52.398.600.999<b class="icon ico_points" title="Боевая мощь"></b><b class="order"></b></td>
<td class="pt3 pb3 pl5 borderr left" data-sort-value="9223372036854775796">Ротвейлер</td>
<td class="p3 right nowrapi" data-sort-value="2620054496">2.620.054.496 <b class="icon ico_glory_small" title="Слава"></b></td>
<td><a href="post.php?m=new&amp;to_id=5074120"><b class="icon ico_mail" title="отправить письмо"></b></a></td>
</tr>




# ищет все теги с CSS классом, в именах которых встречается "itl"
soup.find_all(class_=re.compile("itl"))


'''
from datetime import date
from bs4 import BeautifulSoup
import requests
import lxml
import re

url = 'https://g1.botva.ru/clan_members.php?id=31481'



def main():
    print("[INFO] ")
    page = requests.get(url)
    print(page.status_code)
    html = page.content
    soup = BeautifulSoup(html, "lxml")
    today = date.today()
    fname = "{}.{}.{}".format(today.day, today.month, today.year)
    fname = fname + ".csv"
    f = open(fname, 'w')
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
            if c!='':
                rw.append(c)
                i = i + 1
                if i==5:
                    i = 0
                    e = tuple(rw)
                    all_cols.append(e)
                    rw.clear()
    #print(all_cols)
    f.write(f'{url}\n')
    for r in all_cols:
        f.write(f"{r[0]};{r[2]}\n")
    f.close()
    print('Обработка завершена, проверьте файл с сегодняшней датой')




if __name__ == "__main__":
    main()
