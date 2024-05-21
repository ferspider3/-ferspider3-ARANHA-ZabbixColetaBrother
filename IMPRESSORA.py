#!/usr/bin/python3

import sys
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Abre o arquivo IMPRESSORA.txt para escrita
with open(r'C:\zabbix\IMPRESSORA.txt', 'w') as file:

    # Configurações para o navegador Firefox ser executado em modo headless (sem interface gráfica)
    options = Options()
    options.add_argument('--headless')

    # Inicializa o navegador Firefox com as opções configuradas
    browser = webdriver.Firefox(options=options)

    # Definições de IP da impressora e senha de acesso
    ip = "192.168.0.1"
    senha = "initpass"
    url = f"http://{ip}/general/status.html"

    # Navega até a página de status da impressora
    browser.get(url)
    
    # Encontra o campo de senha e insere a senha
    campo_senha = browser.find_element("xpath", '//*[@id="LogBox"]')
    campo_senha.send_keys(senha)
    
    # Clica no botão de login
    browser.find_element("xpath", '//*[@id="login"]').click()
    
    # Espera 5 segundos para garantir que a página de login foi processada
    time.sleep(5)
    
    # Navega até a página de informações da impressora
    pagina = browser.get(f"http://{ip}/general/information.html?kind=item")
    
    # Espera 4 segundos para garantir que a página de informações foi carregada
    time.sleep(4)
    
    # Faz o parse do código fonte da página usando BeautifulSoup
    contadores = bs(browser.page_source, 'html.parser')

    # Extrai a informação de carga do toner
    cargaToner = str(contadores.find_all('dd')[16])
    
    # Verifica o tamanho do texto extraído e escreve o valor da carga do toner no arquivo
    if len(cargaToner) == 13:
        file.write(str(int(cargaToner[4:7])) + '\n')
    elif len(cargaToner) == 12:
        file.write(str(int(cargaToner[4:6])) + '\n')
    else:
        file.write(str(int(cargaToner[4:5])) + '\n')

    # Fecha o navegador
    browser.quit()
