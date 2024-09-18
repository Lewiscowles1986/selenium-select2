from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver options to use Chromium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)

# Open the Select2 HTML page served by the webserver
driver.get('http://webserver:80')

# Wait for the Select2 container to appear and click on it to open the dropdown
select2_container = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.select2-container'))
)
select2_container.click()

# Wait for the dropdown options to be visible
options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.select2-results__option'))
)

# Loop through the options and select the one you want
for option in options:
    option_text = f"{option.text}"
    if option_text == 'Option 2':
        option.click()
        print(f'Selected: {option_text}')
        break

# Close the driver
driver.quit()
