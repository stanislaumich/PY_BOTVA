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
from datetime import datetime

from beep import mybeep
"""
pip install undetected-chromedriver
"""
tm = 5  # таймаут обновления страницы ускора в секундах
sl = 30  # пауза мин максимально ждать, обычно полчаса
wt = 20  #  в эту минуту запускаемся

def main():
    print("[INFO] Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать ускор")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    try:
        os.mkdir(myp)
    except:
        print("Путь профиля хром уже существует")

    print("Путь профиля Chrome: " + myp)
    #options = webdriver.ChromeOptions()
    opts = uc.ChromeOptions()
    if os.path.exists('s:/home'):
        opts.add_argument(f'--proxy-server=127.0.0.1:3128')
    opts.add_argument(r"--user-data-dir=" + myp)
    opts.add_argument("--profile-directory=BOTVA")
    #opts.add_argument('--headless')
    #  +options.add_argument("start-maximized")
    #  options.add_argument("--headless")
    #  +options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #  +options.add_experimental_option('useAutomationExtension', False)
    #  driver = webdriver.Chrome(options=options)
    driver = uc.Chrome(options=opts)
    stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    print("Логин...  ")
    #  node = driver.find_element(By.CSS_SELECTOR, "h5[class='sc-29427738-0 sc-bdnxRM kgxFZp hBeyeI']")
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    #  element = driver.find_element("name", "email")
    #  element.send_keys(mysettings.login)
    #  element = driver.find_element("name", "password")
    #  element.send_keys(mysettings.passw)
    #  element = driver.find_element("name", "server")
    #  element.send_keys("t")
    element = driver.find_element(By.XPATH, '//*[@id="auth_form_email"]/form/div[4]/div/input')
    element.submit()
    print(f"Fly")
    sleep(5)
    #  element = driver.find_element(By.XPATH, '//*[@id="m53"]')
    #  element.click()
    try:
        driver.get("https://g1.botva.ru/event.php?a=airships")
        sleep(5)
        enr = driver.find_element(By.CLASS_NAME, "img_money_airships_energy")
        enr.click()
        sleep(3)
        enr = driver.find_element(By.CLASS_NAME, "img_money_airships_energy")
        enr.click()
        sleep(3)
        enr = driver.find_element(By.CLASS_NAME, "img_money_airships_energy")
        enr.click()
    except:
        print("Error")

    #  print(f"Ждем минуту - {wt=}")

    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
