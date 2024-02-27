import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


TINDER_URL = "https://tinder.com/"
EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

# Opening the tinder url
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDER_URL)

# Accepting all cookies
time.sleep(1)
cookies_button = driver.find_element(By.XPATH, value='//*[@id="c-1398387530"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies_button.click()

# Pressing login button 
login_button = driver.find_element(By.LINK_TEXT, value="Log in")
login_button.click()
time.sleep(1)
fb_button = driver.find_element(By.XPATH, value='//*[@id="c-1177047094"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_button.click()

time.sleep(2)

# How to swith to a pop up window
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])

# Login with facebook
email_input = driver.find_element(By.ID, value="email")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, value="pass")
password_input.send_keys(PASSWORD, Keys.ENTER)

time.sleep(2)
driver.switch_to.window(all_windows[0])

time.sleep(3)
location_button = driver.find_element(By.XPATH, value='//*[@id="c-1177047094"]/main/div/div/div/div[3]/button[1]')
location_button.click()

time.sleep(3)
notification_button = driver.find_element(By.XPATH, value='//*[@id="c-1177047094"]/main/div/div/div/div[3]/button[2]')
notification_button.click()

time.sleep(6)
actions = ActionChains(driver)
for i in range(100):
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()
    time.sleep(1)

driver.quit()
