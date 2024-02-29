import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
time.sleep(4)

#element = driver.find_element(By.XPATH,"//a[@id='formAnchor1434677811']")
#driver.switch_to.frame(element)

goto = driver.find_element(By.XPATH, "RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();", goto)
time.sleep(2)


driver.find_element(By.XPATH,"RESULT_FileUpload-10").send_keys("Desktop/download.jpg ")