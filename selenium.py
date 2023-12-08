import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set location of the webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.get('https://aws.amazon.com/')
driver.maximize_window()

# Find and click on the "Sign In to the Console" button
sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign In')
sign_in_button.click()

# Click on the "Sign-in using Secure SSO" link
sso_link = driver.find_element(By.LINK_TEXT, 'Sign-in using Secure SSO')
sso_link.click()

# Wait for the SSO login page to load
time.sleep(5)

# Enter the SSO start URL
sso_start_url = driver.find_element(By.ID, 'username')
sso_start_url.send_keys('https:sso-url.com')
sso_start_url.send_keys(Keys.RETURN)

# Wait for the SSO login page to load
time.sleep(5)

# Enter the SSO region
sso_region = driver.find_element(By.ID, 'username')
sso_region.send_keys('ap-southeast-2')
sso_region.send_keys(Keys.RETURN)

# Wait for the SSO login page to load
time.sleep(5)

# Enter the SSO account ID
sso_account_id = driver.find_element(By.ID, 'username')
sso_account_id.send_keys('111222333444')
sso_account_id.send_keys(Keys.RETURN)

# Wait for the SSO login page to load
time.sleep(5)

# Enter the SSO role name
sso_role_name = driver.find_element(By.ID, 'username')
sso_role_name.send_keys('sso-role')
sso_role_name.send_keys(Keys.RETURN)

# Wait for the sign-in process to complete
time.sleep(5)

# Perform subsequent actions using the assumed IAM role
# For example, you can navigate to AWS services and interact with them

# Take a screenshot as an example
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_name = f"aws_console_{timestamp}.png"
driver.save_screenshot(screenshot_name)

# driver.quit()
