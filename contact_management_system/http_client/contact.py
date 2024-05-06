import requests


domain = "http://localhost:8000"
get_users_list_url = "/user"
requests.get(url=(domain + get_users_list_url))