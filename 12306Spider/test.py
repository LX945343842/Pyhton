import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)
driver.find_element_by_link_text("账号登录").click()
username = driver.find_element_by_id("J-userName")
username.clear()
username.send_keys("15558975701")
password = driver.find_element_by_id("J-password")
password.clear()
password.send_keys("hahaguangzhu01.")
time.sleep(5)
driver.find_element_by_link_text("立即登录").click()
time.sleep(5)
print("登录成功！")