# ARANHA-ZabbixColetaBrother

![Windows](https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-E34F26?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Coleta de Nível de Impressora Brother

Este script é utilizado para coletar o nível de toner de uma impressora Brother. Ele foi desenvolvido em Python e utiliza as bibliotecas Selenium e BeautifulSoup, juntamente com o navegador Firefox em modo headless.

### Requisitos

- Python 3
- Selenium
- BeautifulSoup4
- Navegador Firefox
- Geckodriver (compatível com a versão do Firefox)

### Instalação

Instale as bibliotecas necessárias:

```
pip install selenium beautifulsoup4
```

Faça o download do Geckodriver a partir do site oficial e adicione-o ao seu PATH: https://github.com/mozilla/geckodriver/releases

Após a instalação, o script irá coletar o nível de toner da impressora Brother especificada e salvar essa informação no arquivo `C:\zabbix\IMPRESSORA.txt` ou `\usr\home\IMPRESSORA.txt` (Ou onde desejar, basta alterar o caminho).

Para testar a coleta, basta executar:

```
python IMPRESSORA.py
```

Para poder realizar a leitura do txt, adicione o seguinte paramêtro no seu Zabbix no `C:\zabbix\zabbix_agentd.conf` ou `/etc/zabbix/zabbix_agentd.conf`:

```
UserParameter=IMPRESSORA,type C:\zabbix\IMPRESSORA.txt
```

## Executando

Adicione o item conforme a imagem abaixo para poder coletar os dados e exibir nos dados recentes:

<img src="https://github.com/ferspider3/ARANHA-ZabbixColetaBrother/blob/main/zabbix.png" alt="Exemplo Zabbix">




