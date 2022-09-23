from sys import call_tracing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
carteiraFrom = []
driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a")

txHashPageList = driver.find_elements(By.CLASS_NAME, 'myFnExpandBox_searchVal')
sleep(1)

for txHash in txHashPageList:
  sleep(1)
  driver.get("https://bscscan.com/tx/"+txHash.text)  
  sleep(1)
  carteiraAprovada = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[7]/div[2]/ul/li/div/a[2]/span').text
  sleep(1)
  if carteiraAprovada == "0x627621F9d14809F258Ce09f31A2be70a9cB1b7C8" or carteiraAprovada == "0x06569e99AEEe8D1f914914A00DeA91Ad498fA3eC" or carteiraAprovada == "0x6f42895f37291ec45f0a307b155229b923ff83f1":  
    carteiraFrom.append(driver.find_element(By.ID, 'addressCopy').text)
    
  sleep(1)
  driver.close()
  sleep(2)
  driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a")
  sleep(2)

sleep(2)
print(carteiraFrom)