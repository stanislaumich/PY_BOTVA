'''
'''
from time import sleep
import os
from selenium.webdriver.common.by import By
import configparser
from selenium import webdriver
import pickle
''''''

# пауза между открытиями
pause = 6
def main():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("s:\\config.ini")  # читаем конфиг
    basepath = config["PATH"]["workdir"]
    try:
        os.mkdir(basepath)
    except:
        print("Проверка рабочей папки")
    finally:
        print(" ")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: "+myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir="+myp)
    options.add_argument("--profile-directory=BOTVA")

    driver = webdriver.Chrome(options=options)#chrome_
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
    driver.get("https://g1.botva.ru/index.php?pandora=253233098&type=gold")
    sleep(3)
    m = driver.find_element(By.CLASS_NAME, "modlunar")
    m.click()
    print(1)
    sleep(pause)
    for i in range(2, N + 1):
        m.click()
        sleep(pause)
        print(i)

if __name__ == "__main__":
    main()
