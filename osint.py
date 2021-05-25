from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
termo_pesquisa = input("Digite o termo para pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

#modulo de consulta - Portal da Transparencia Gov Br
driver.get(f'http://www.portaltransparencia.gov.br/busca?termo="{termo_pesquisa}"') #entrar no portal 
resultado = driver.find_element_by_id('countResultados')
print(f'Possui {resultado.text} resultados no Portal da Transparência do Governo Federal.')

#pesquisa no Google 
driver.get(f'https://www.google.com/search?q={termo_pesquisa}&lr=lang_pt') #site para fazer scraping
titulo_site = driver.find_element_by_partial_link_text('mortaza')

print(titulo_site.text)
