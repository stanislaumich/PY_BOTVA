from time import sleep
import random
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
import mysettings

N = 160 #количество серий из 3 боёв (включено зелье + гриб + бодалка раз в 30 сек, если нет, надо менять задержки в программе

def main():
		print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать прокачку")
		#config = configparser.ConfigParser()  # создаём объекта парсера
		#config.read("config.txt")  # читаем конфиг

		myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
		print("Путь профиля Chrome: " + myp)
		options = webdriver.ChromeOptions()
		options.add_argument("--allow-profiles-outside-user-dir")
		options.add_argument(r"user-data-dir=" + myp)
		options.add_argument("--profile-directory=BOTVA")
		driver = webdriver.Chrome(options=options)
		print("Логин...  ")

		driver.get("http://botva.ru")
		element = driver.find_element(By.CLASS_NAME, "sign_in")
		element.click()
		element = driver.find_element("name", "email")
		#element.send_keys(config["LOGIN"]["username"])
		element.send_keys(mysettings.login)
		element = driver.find_element("name", "password")
		#element.send_keys(config["LOGIN"]["password"])
		element.send_keys(mysettings.passw)
		element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
		element.submit()
		sleep(random.random() * 3)
		
			
		for i in range(N):
			driver.get("https://g1.botva.ru/dozor.php")
			sleep(2)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_arow7")
			element1.click()
			sleep(random.random() * 2+1)
			#elements = driver.find_elements(By.CLASS_NAME, "cmd_arow7")
			#element.click()
			#sleep(random.random() * 3)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_row3")
			element1.click()
			sleep(random.random() * 3)
			
			driver.get("https://g1.botva.ru/dozor.php")
			sleep(2)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_arow7")
			element1.click()
			sleep(random.random() * 2+1)
			#elements = driver.find_elements(By.CLASS_NAME, "cmd_arow7")
			#element.click()
			#sleep(random.random() * 3)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_row3")
			element1.click()
			sleep(random.random() * 3)
			
			driver.get("https://g1.botva.ru/dozor.php")
			sleep(2)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_arow7")
			element1.click()
			sleep(random.random() * 2+1)
			#elements = driver.find_elements(By.CLASS_NAME, "cmd_arow7")
			#element.click()
			#sleep(random.random() * 3)
			element1 = driver.find_element(By.CLASS_NAME, "cmd_row3")
			element1.click()
			sleep(random.random() * 3)
			sleep(16)
				
		
if __name__ == "__main__":
    main()
