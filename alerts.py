import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
time.sleep(3)

#accept alert
driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
driver.switch_to.alert.accept()
msg=driver.find_element(By.XPATH,"//p[text()='You pressed OK!']")
print(msg.text)

#cancle alert
driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
driver.switch_to.alert.dismiss()
msg=driver.find_element(By.XPATH,"//p[text()='You pressed Cancel!']")
print(msg.text)


driver.get("http://demo.automationtesting.in/Alerts.html")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//a[text()='Alert with Textbox ']").click()
driver.find_element(By.XPATH,"//button[text()='click the button to demonstrate the prompt box ']").click()
driver.switch_to.alert.send_keys("jrvsaikiran")
driver.switch_to.alert.accept()
data=driver.find_element(By.XPATH,"//p[@id='demo1']")
print(data.text)
#driver.quit()