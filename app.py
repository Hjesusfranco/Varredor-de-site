# repita os passos manuais, usando código:



# 4 - repetir para todos os produtos da pagina
# 5 - guardar informações em arquivo de texto (CSV)
# XPATXH(identificador de elementos no site)
#//tag[@atributo='valor']

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

# 1 - entrar no site: https://clone-olx-devaprender.netlify.app/
driver = webdriver.Chrome()
driver.get('https://clone-olx-devaprender.netlify.app/')
sleep(5)

# 2 - anotar os nomes dos produtos
produtos = driver.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")

# 3 - anotar os preços dos produtos
precos = driver.find_elements(By.XPATH, "//span[@class='text-2xl font-bold text-gray-900']")

for produto, precos in zip(produtos,precos):
    with open('preços.csv','a', encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{precos.text}{os.linesep}')
input('')
