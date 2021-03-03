#!/usr/bin/python3
from selenium import webdriver
import time

url = "http://101.37.32.116:20212/"
# url = "http://127.0.0.1:8081/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=options)

while True:
    try:
        driver.get(url + "login")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("admin is not administrator :-)")
        driver.find_element_by_id("submit").click()
    except Exception as e:
        print(time.asctime(time.localtime(time.time())))
        print(e)
        print("***************************************")
    time.sleep(3 * 60)
# never reach
driver.quit()
