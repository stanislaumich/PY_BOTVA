'''
'''
import mysettings
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium_stealth import stealth
import undetected_chromedriver as uc
from beep import mybeep
''''''

# пауза между открытиями
pause = 13
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
    try:
        element = driver.find_element(By.CLASS_NAME, "sign_in")
        element.click()
        element = driver.find_element("name", "email")
        element.clear()
        element.send_keys(mysettings.login)
        element = driver.find_element("name", "password")
        element.clear()
        element.send_keys(mysettings.passw)
        #  element = driver.find_element("name", "server")
        #  element.send_keys("t")
        sleep(2)
        #element = driver.find_element(By.XPATH, '//*[@id="auth_form_email"]/form/div[4]/div/input')
        #element.submit()
    except:
        print("Не найдено")

    print("Поехали")
    driver.get("https://avatar.botva.ru/dozor.php")
    sleep(1)
    t = True
    r = 0
    while t:
        m = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/center/form/div[1]/div/div/span/input")
        m.click()
        print(1)
        mybeep()
        sleep(pause)
        r = r+1
        if r > 20:
            t = False

    print("ЗАВЕРШИЛ 20")

if __name__ == "__main__":
    main()
