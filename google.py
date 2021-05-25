from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
termo_pesquisa = input("Digite o termo para pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

#pesquisa no Google 
driver.get(f'https://www.google.com/search?q={termo_pesquisa}&lr=lang_pt') #site para fazer scraping
titulo_site = driver.find_element_by_partial_link_text('mortaza')

print(titulo_site.text)
