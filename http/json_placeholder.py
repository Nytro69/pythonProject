import requests

# /posts	100 posts
# /comments	500 comments
# /albums	100 albums
# /photos	5000 photos
# /todos	200 todos
# /users	10 users

api_base = "https://jsonplaceholder.typicode.com"

def get_users():
    url = f'{api_base}/users'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None

def get_user_by_id(user_id):
    url = f'{api_base}/users/{user_id}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None



def create_post():
    pass


url = f'{api_base}/posts'
data = {
    "userId": 1,
    "title": "My Post",
    "body": "This is my post jsajbdhfhkasd"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())