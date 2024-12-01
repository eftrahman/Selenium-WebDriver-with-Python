from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

# Wait for user input
input("Press Enter to close the browser...")
