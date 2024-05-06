import pprint

import requests
from .. import urls as u


def get_request(**query_params):
    response = requests.get()


def post_request(url, data):
    response = requests.post(url, data)


# ----------------------------------------------( fetch contact ) -------------------------------------------------
url = u.FETCH_CONTACTS_URL
payload = {
    "user_id": 4,
    "name": "Sara Jackson"
}
response = requests.get(url, params=payload)
pprint.pprint(response.json())
print(response.cookies)
# print(requests.Session())


# ----------------------------------------------( add contact ) -------------------------------------------------
url = u.ADD_CONTACT_URL

payload = {
    "name": "Jafar",
    "user_id": "1",
    "email": "Jafar_ye_dande@gmail.com",
    "number1": "5585858585858",
    "number2": "79797979",
}
response = requests.post(url, data=payload)
print(response)

session = requests.Session()
retry = Retry(connect=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.keep_alive = False
session.mount('http://', adapter)
session.mount('https://', adapter
