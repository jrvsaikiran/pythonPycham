import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
time.sleep(5)


rows=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))

columns= len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td"))      #count no.of columns

print("no.of rows",rows)
print("no.of columns",columns)

print("BookName"+"       "+"Author"+"        "+"Subject"+"        "+"price")
for r in range(2,rows+1):
    for c in  range(1,columns+1):
        value= driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='        ')
    print()


driver.close()

