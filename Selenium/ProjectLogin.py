from selenium import webdriver
import time

def login():
    """登录"""
    dirver = webdriver.Chrome()
    dirver.find_element_by_id("account").send_keys("ctjrdzsw")
    time.sleep(1)
    dirver.find_element_by_id("password").send_keys("111111")
    time.sleep(1)
    dirver.find_element_by_xpath("//*[@id=\"login_txt\"]").click()
    time.sleep(1)
    print(dirver.title)