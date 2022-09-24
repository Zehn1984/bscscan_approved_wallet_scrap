from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
carteiraFrom = []
driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=1")
sleep(1)
maxPage = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div/div[2]/nav/ul/li[3]/span/strong[2]').text

for n in range(int(maxPage)):
  driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=" + str(n + 1))
  txHashPage = driver.find_elements(By.CLASS_NAME, 'myFnExpandBox_searchVal') 
  # Eh necessario guardar os dados desestruturados antecipadamente em um array pois quando se muda de pagina, todo DOM eh apagado, e junto, nossa variavel.
  txHashArr = [i.text for i in txHashPage]

  for txHash in txHashArr:
    
    #print(len(txHashArr))
    driver.get("https://bscscan.com/tx/"+txHash)
    sleep(1)
    # Foi necessario usar find_element[S] para retornar uma array vazia, e nao uma excessao com erro
    carteiraAprovada = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[7]/div[2]/ul/li/div/a[2]/span')
    # Assim pode-se fazer uma confirmacao, evitando o erro
    if carteiraAprovada:
      #print(carteiraAprovada[0].text)
      if carteiraAprovada[0].text == "0x627621F9d14809F258Ce09f31A2be70a9cB1b7C8" or carteiraAprovada[0].text == "0x06569e99AEEe8D1f914914A00DeA91Ad498fA3eC":  
        carteiraFrom.append(driver.find_element(By.ID, 'addressCopy').text)
    driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=" + str(n + 1))
    sleep(1)
    if txHash == txHashArr[len(txHashArr) - 1]:
      break
  print(n)
  n += 1
sleep(1)
print(carteiraFrom)