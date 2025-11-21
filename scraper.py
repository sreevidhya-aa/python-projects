from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

print("Opening IMDb...")
driver.get("https://www.imdb.com/chart/top/")


print("Chrome will stay open for 0.5 minutes...")
time.sleep(30)

print("Closing browser now!")
driver.quit()
