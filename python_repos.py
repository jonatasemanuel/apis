import requests


# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável
response_dict = r.jason()
# Processa o resultado
print(response_dict.keys())
