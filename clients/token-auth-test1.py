import requests


def client():
    # credentials = {'username': 'admin', 'password': '141191Cj.'}

    # response = requests.post(
    #     'http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    token_h = 'Token e8513ba219cdf23f52df18f4d799cf5b710a18e6'
    headers = {'Authorization': token_h}

    response = requests.get(
        'http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
