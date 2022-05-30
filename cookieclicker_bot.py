from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_service = Service(executable_path="/Users/garylin/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=driver_service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
while True:
    cookie.click()

    if time.time() > timeout:
        timeout = time.time() + 5
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        items = driver.find_elements(By.CSS_SELECTOR, "#store div b")[:-1]
        items_dict = {item.text.split(" ")[0]: item for item in items}
        cost = {item.text.split(" ")[0]: int(item.text.split(" ")[-1].replace(",", "")) for item in items}
        for item in reversed(cost):
            if cost[item] < money:
                items_dict[item].click()
                break
        cookies_per_sec = driver.find_element(By.ID, "cps")
        print(cookies_per_sec.text)
