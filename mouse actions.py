import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://www.flipkart.com/samsung-galaxy-f13-coming-soon-hgh33-79kd-store?param=3571&otracker=hp_bannerads_1_2.bannerAdCard.BANNERADS_Mob_AW_Samsung_F13_Y3TFQB1X9QK8")
driver.maximize_window()

driver.implicitly_wait(5)
#mouseover
men= driver.find_element(By.XPATH,"//span[text()='Men']")
action = ActionChains(driver)
action.move_to_element(men).perform()

time.sleep(3)

#double click and right click
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
time.sleep(5)
clickontextbutton= driver.find_element(By.XPATH,"//button[text()='Copy Text']")
action.double_click(clickontextbutton).perform()
action.context_click(clickontextbutton).perform()
time.sleep(3)


#drag and drop

sourse=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
target=driver.find_element(By.XPATH,"//p[text()='Drop here']")
print(sourse.text)
print(target.text)
action.drag_and_drop(sourse,target).perform()


verify= driver.find_element(By.XPATH,"//p[text()='Dropped!']")
print(verify.text)
time.sleep(3)
driver.close()

