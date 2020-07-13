# import requests
#
# # Поиск местонахождения для запросов на GitHub
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Анализ некоторых атрибутов местонахождения запросов
# json_response = response.json()
# print(json_response)
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')  # Python 3.6+
