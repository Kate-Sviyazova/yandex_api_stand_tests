import requests

import configuration
import data
import sender_stand_request


# Получение токена пользователя
def get_user_token ():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)
    response_token = gaet_user_token()
    data.authToken ["Authorization"] = "Bearer" + response_token.json()["authToken"]

#Функция для изменения значения параметра "name" в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#Функция для позитивной проверки
def positive_assert (name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.authToken)
    assert kit_response.status_code == 201
    assert kit_response.json() ["name"] == name

#Функция для негативной проверки
def negative_assert (kit_body):
    #kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, data.authToken)
    assert response.status_code == 400

