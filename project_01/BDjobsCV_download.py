from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()

username = "email"
password = "password"

driver.get("https://www.bdjobs.com")
title01 = driver.title
print(title01)

dropdown01 = driver.find_element(By.XPATH,"//a[@role='button'][contains(text(),'Sign in')]")
dropdown01.click()
sign_in_button = driver.find_element(By.XPATH,"//a[@class='btn slu-btn'][normalize-space()='Sign in']")
sign_in_button.click()
print("in the sign in page")

usernameBox = driver.find_element(By.ID,"TXTUSERNAME")
usernameBox.send_keys(username)
continueButton = driver.find_element(By.XPATH,"//input[@value='Continue']")
continueButton.click()
print("username completed")

passwordBox = driver.find_element(By.ID,"TXTPASS")
passwordBox.send_keys(password)
SignInButton = driver.find_element(By.XPATH,"//input[@value='Sign in']")
SignInButton.click()
print("sign in completed")

dropdown02 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "userDetailsDropdown"))
)
dropdown02.click()
profileButton = driver.find_element(By.LINK_TEXT,"View Profile")
profileButton.click()
print("In the Profile page")
driver.switch_to.window(driver.window_handles[-1])

downloadCVButton= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Word Format']"))
)
downloadCVButton.click()

print("*** -> CV download completed ***")




input("press enter to close")