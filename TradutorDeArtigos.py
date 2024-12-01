import requests
from bs4 import BeautifulSoup

def extarir_texto_da_pagina(url):
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      for script in soup(['script', 'style']):
        script.decompose()
      texto = soup.get_text()
      linhas = (line.strip() for line in texto.splitlines())
      parts = (phrase.strip() for line in linhas for phrase in line.split('  '))
      texto = '\n'.join(linha for linha in linhas if linha)

      return texto
    else:
        raise Exception(f'Erro ao acessar a página {url}')
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()
    return texto

extarir_texto_da_pagina('https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo')

from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint = "YOUR_ENDPOINT",
    api_key = "OUR_API_KEY",
    api_version= "API_VERSION",
    deployment_name = "NAME",
    max_retries=0 
)

def translate_articles(text, lang):
  messages = [
      ('system', 'Você atua como um tradutor de textos'),
      ('user', f'Traduza o {text} para o idioma {lang} e responda em markdown')
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content


translate_articles('Hello World', 'pt')

url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extarir_texto_da_pagina(url)
article = translate_articles(text, 'pt')

print(article)