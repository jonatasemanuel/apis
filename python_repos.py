import requests


# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Analisa o primeiro repositório:
# repo_dict = repo_dicts[0]
# print(f'\nKeys: {len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#    print(key)

# Mostra todos os repositórios possiveis na tela:
for repo_dict in repo_dicts:
    print('\nSelected information about first repository: ')
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

