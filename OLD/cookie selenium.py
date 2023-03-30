Сохраняем сессию.

import pickle
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.quora.com')
# login code
pickle.dump(driver.get_cookies() , open("QuoraCookies.pkl","wb"))



Добавляем её при следующем использовании

import pickle
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.quora.com')
for cookie in pickle.load(open("QuoraCookies.pkl", "rb")):
    driver.add_cookie(cookie)