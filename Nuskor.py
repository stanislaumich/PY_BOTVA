import random
import sys
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import mysettings
import traceback
from selenium.webdriver.firefox.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc

from beep import mybeep
"""
pip install undetected-chromedriver
"""
tm = 7  # таймаут обновления страницы ускора в секундах
sl = 17  # пауза мин


def main():
    print("[INFO] Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать ускор")
    print(f"Запускаем паузу секунд - {sl=}")
    ps = 60 * sl
    for i in range(sl):
        sleep(60)
        print(f"Минутка прошла {i=}")
    # sleep(ps)
    print("Поехали")
    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    try:
        os.mkdir(myp)
    except:
        print("Путь профиля хром уже существует")

    print("Путь профиля Chrome: " + myp)
    options = webdriver.ChromeOptions()
    #  +options.add_argument("start-maximized")
    #  options.add_argument("--headless")
    #  +options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #  +options.add_experimental_option('useAutomationExtension', False)
    #  driver = webdriver.Chrome(options=options)
    driver = uc.Chrome(options=options)
    stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    print("Логин...  ")

    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys(mysettings.login)
    element = driver.find_element("name", "password")
    element.send_keys(mysettings.passw)
    element = driver.find_element("name", "server")
    element.send_keys("t")
    element = driver.find_element(By.XPATH, '//*[@id="auth_form_email"]/form/div[4]/div/input')
    element.submit()
    sleep(random.random() * 2 + 0.5)
    driver.get("https://g1.botva.ru/monster.php?a=monsterpve")

    t = True
    while t:
        try:
            element = driver.find_element(By.XPATH,
                                          "/html/body/div[5]/div[3]/div[2]/div[2]/div[2]/div[4]/form/input[3]")
            t = element.click()
            #  t = False
            print("УРАА!!")
            mybeep()
        except:
            print("Не найдено")
        sleep(tm)
        driver.get("https://g1.botva.ru/monster.php?a=monsterpve")
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()