import requests

def consulta():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    print(response.status_code)
    print(response.json())
    for pessoa in response.json():
        print(pessoa['userId'], pessoa['Id'], pessoa['title'], pessoa['body'])


def insere():
    userId = 1
    id = 101
    title = 'Post de Rodrigo'
    body = 'Inserindo um post Ipsum maravilis'
    post = {'userId': userId, 'Id': id, 'title': title, 'body': body}
    response = requests.post('https://jsonplaceholder.typicode.com/posts/', json=post)
    print(response.status_code)
    print(response.json())

insere()
#consulta()
