import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def change_firstName(name):
    body_test = data.user_body.copy ()
    body_test ["firstName"] = name
    return body_test

def post_new_client_kit (kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                         headers=auth_token,
                         json=kit_body)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())