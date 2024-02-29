import data
import sender_stand_request


# Функция для изменения значения в параметре firstName в теле запроса
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["first_name"] = first_name
    return current_body


def positive_assert(first_name):
    user_body = sender_stand_request.change_firstName(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    print(str_user)


def negative_assert_symbol(first_name):
    user_body = sender_stand_request.change_firstName(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                              "Имя может содержать только русские или латинские буквы, " \
                                              "длина должна быть не менее 2 и не более 15 символов"


def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_1_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")


# Тест 2. Успешное создание пользователя
# Параметр fisrtName состоит из 15 символов
def test_2_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")


# Тест 3. Ошибка при создании пользователя
# Параметр firstName состоит из 1 символа
def test_3_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("А")


# Тест 4. Ошибка при создании пользователя
# Параметр firstName состоит из 16 символов
def test_4_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")


# Тест 5. Успешное создание пользователя
# Параметр firstName состоит из английских букв
def test_5_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("Vova")


# Тест 6. Успешное создание пользователя
# Параметр firstName состоит из русских букв
def test_6_create_user_russian_letter_in_first_name_get_success_response():
    positive_assert("Вова")


# Тест 7. Ошибка при создании пользователя
# В параметр firstName входят пробелы
def test_7_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Иваа аааан")


# Тест 8. Ошибка при создании пользователя
# В параметр firstName входят спецсимволы
def test_8_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")


# Тест 9. Ошибка при создании пользователя
# В параметр firstName входят цифры
def test_9_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123Иван")


# Тест 10. Ошибка при создании пользователя
# Параметр firstName не передан
def test_10_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)


# Тест 11. Ошибка при создании пользователя
# Параметр firstName пустое значение
def test_11_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)


# Тест 12. Ошибка при создании пользователя
# В параметр firstName передан другой тип параметра
def test_12_create_user_has_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
