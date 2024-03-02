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
    assert kit_response.json()["name"] == name

#Функция для негативной проверки
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, data.authToken)
    assert response.status_code == 400

# Тест 1. Успешное создание набора пользователя
# Параметр name состоит из 1 символа
def test_1_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора пользователя
# Параметр name состоит из 551 символов
def test_2_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                    "abcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Набор пользователя не создан:
# Параметр name состоит из 0 символов
def test_3_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Тест 4. Набор пользователя не создан:
# Параметр name состоит из 512 символов
def test_4_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    negative_assert_code_400(kit_body)

# Тест 5. Успешное создание набора пользователя
# Параметр name состоит из английских букв
def test_5_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора пользователя
# Параметр name состоит из русских букв
def test_6_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора пользователя
# Параметр name состоит из спецсимволов
def test_7_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("№%@,")

# Тест 8. Успешное создание набора пользователя
# Параметр name с пробелами внутри
def test_8_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")

# Тест 9. Успешное создание набора пользователя
# Параметр name состоит цифр
def test_9_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Набор пользователя не создан:
# Параметр name не передан в запросе
def test_10_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Тест 11. Набор пользователя не создан:
# Передан другой тип параметра (число):
def test_11_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)