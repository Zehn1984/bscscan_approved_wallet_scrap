from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import uniform

driver = webdriver.Firefox()
carteiraFromArr = []
driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=1")
sleep(uniform(1,2))
maxPage = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div/div[2]/nav/ul/li[3]/span/strong[2]').text
print("Iniciando pesquisa na pagina 1...")

for n in range(int(maxPage)):
  driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=" + str(n + 1))
  txHashPage = driver.find_elements(By.CLASS_NAME, 'myFnExpandBox_searchVal') 
  # Eh necessario guardar os dados desestruturados antecipadamente em um array pois quando se muda de pagina, todo DOM eh apagado, e junto, nossa variavel.
  txHashArr = [i.text for i in txHashPage]

  for txHash in txHashArr:
    
    driver.get("https://bscscan.com/tx/"+txHash)
    sleep(uniform(1,2))
    # Foi necessario usar find_element[S] para retornar uma array vazia, e nao uma excessao com erro
    carteiraAprovada = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[7]/div[2]/ul/li/div/a[2]/span')
    # Assim pode-se fazer uma confirmacao, evitando o erro
    if carteiraAprovada:
      if carteiraAprovada[0].text == "0x627621F9d14809F258Ce09f31A2be70a9cB1b7C8" or carteiraAprovada[0].text == "0x06569e99AEEe8D1f914914A00DeA91Ad498fA3eC" or carteiraAprovada[0].text == "0xda0ae0710b080ac64e72fa3ec44203f27750f801":  
        carteiraFromArr.append(driver.find_element(By.ID, 'addressCopy').text)
        with open("carteiras_from.txt", "w") as carteiras_from:
          carteiras_from.write(str(carteiraFromArr))
        lastAppend = ("\nUltima insercao foi da txHash " + str(txHash) + " da pagina " + str(n + 1))
        with open("carteiras_from.txt", "a") as carteiras_from:
          carteiras_from.write(lastAppend)          
        print(carteiraFromArr)
    driver.get("https://bscscan.com/txs?a=0xa045e37a0d1dd3a45fefb8803d22457abc0a728a&ps=10&p=" + str(n + 1))
    sleep(uniform(1,2))
    if txHash == txHashArr[len(txHashArr) - 1]:
      break
  print("Pagina " + str(n + 1) + " finalizada, iniciando pagina " + str(n+2))
  n += 1
sleep(uniform(1,2))
print(carteiraFromArr)