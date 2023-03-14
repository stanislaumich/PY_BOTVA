'''
'''
from time import sleep
import os
from selenium.webdriver.common.by import By
import configparser
from selenium import webdriver
import mysettings
''''''
uagent = ""
def main():
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

    driver = webdriver.Chrome(chrome_options=options)
    print("Логин...  ")
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys(mysettings.login)
    element = driver.find_element("name", "password")
    element.send_keys(mysettings.passw)
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
    ''''''
    driver.get("https://g1.botva.ru/dozor.php")
    sleep(2)
    element = driver.find_element(By.ID, "watch_find")
    element.click()
    sleep(3)
    driver.get("https://g1.botva.ru/dozor.php")
    sleep(2)
    element = driver.find_element(By.ID, "watch_find")
    element.click()
    sleep(3)
    driver.get("https://g1.botva.ru/dozor.php")
    sleep(2)
    element = driver.find_element(By.ID, "watch_find")
    element.click()
    sleep(3)
    ''''''

if __name__ == "__main__":
    main()
