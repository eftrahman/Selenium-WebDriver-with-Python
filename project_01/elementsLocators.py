from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://selenium.dev")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium" == title

driver.findElement(By.xpath("#APjFqb"))



input("enter to close your browser")