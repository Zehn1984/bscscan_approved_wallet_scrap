from sys import call_tracing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://bscscan.com/tx/0x6330338ce66dd4257b5c379719074d2b498879a4449d6d403f66daf1522b52c1")

carteiraFrom = driver.find_element(By.ID, 'addressCopy').text

print(carteiraFrom)