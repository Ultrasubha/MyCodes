from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome webdriver and open Google Play Store
driver = webdriver.Chrome()
driver.get("https://play.google.com/store")

# Find search box and enter search query
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='q']")))
search_box.send_keys("Genshin Impact")
search_box.submit()

# Click on the first result
first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='search-result-list'] a")))
first_result.click()

# Fetch URL of the page and print as string
url = driver.current_url
print("The URL of the page is:", url)

# Close the webdriver
driver.quit()
