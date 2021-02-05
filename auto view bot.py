import selenium
from selenium import webdriver
import time


def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    page = driver.get("https://letstalkmenstyle.home.blog/")
    time.sleep(5)
    driver.close()


while(True):
    main()
