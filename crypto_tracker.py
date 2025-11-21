from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://coinmarketcap.com/")
time.sleep(5)  


rows = driver.find_elements(By.XPATH, '//tbody/tr')

names, prices, changes, market_caps = [], [], [], []


for row in rows[:10]:  
    name = row.find_element(By.XPATH, './/p[@class="coin-item-symbol"]').text
    price = row.find_element(By.XPATH, './/div[@class="sc-b3fc6b7-0 dzgUIj"]').text
    change = row.find_element(By.XPATH, './/span[contains(@class, "sc-97d6d2ca-0")]').text
    market_cap = row.find_element(By.XPATH, './/span[@class="sc-11478e5d-1 jPHjZw"]').text

    names.append(name)
    prices.append(price)
    changes.append(change)
    market_caps.append(market_cap)


data = pd.DataFrame({
    "Coin Name": names,
    "Price": prices,
    "24h Change": changes,
    "Market Cap": market_caps
})

data.to_csv("crypto_data.csv", index=False)
print("Data saved to crypto_data.csv!")


driver.quit()
