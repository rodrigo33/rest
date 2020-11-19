import requests

def consulta():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    print(response.status_code)
    print(response.json())
    for pessoa in response.json():
        print(pessoa['userId'], pessoa['Id'], pessoa['title'], pessoa['body'])


consulta()
