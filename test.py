import requests
import json

addr = 'http://127.0.0.1:5000'


def auth(username, password):
    url = addr + '/auth'
    headers = {'Content-Type': 'application/json'}
    payload = '{"username": "%s", "password": "%s"}' % (username, password)
    r = requests.post(url, data=payload, headers=headers)
    return json.loads(r.text)['access_token']


def open_page(url, access_token=''):
    if access_token:
        headers = {"Authorization": "JWT " + access_token}
        print(requests.get(url, headers=headers).text)
    else:
        print(requests.get(url).text)


if __name__ == '__main__':
    open_page(addr + '/protected')
    token = auth('user1', 'qwerty')
    print(token)
    open_page(addr + '/protected', token)
