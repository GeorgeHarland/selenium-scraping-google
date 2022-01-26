from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings('ignore')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

driver.get("https://google.com")
print(driver.title)

# Find the search bar
search_bar = driver.find_element_by_name("q")

search_bar.send_keys(Keys.CLEAR)
search_bar.send_keys("github")
search_bar.send_keys(Keys.ENTER)
print(driver.title)