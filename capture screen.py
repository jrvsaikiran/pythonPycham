import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("F:\pic.jpg") #both jpg,png can capture
driver.get_screenshot_as_file("F:\pic1.png")   #only png





time.sleep(1)
driver.close()





