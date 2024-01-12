import requests


def randomusers(n: int, gender: str) -> list[dict]:
    payload = {
        'results': n,
        'gender': gender
    }
    url = 'https://randomuser.me/api'
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        users = []
        for user in response.json()['results']:
            users.append({
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'image': user['picture']['large']
            })

        return users
    