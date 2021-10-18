# pytest -v --driver Chrome --driver-path C:/1/chromedriver test_selenium_petfriends.py

import pytest
from selenium import webdriver
from settings import valid_email, valid_password
import time


@pytest.fixture(autouse=True)
def chrome_setup():
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает явные и неявные ожидания,
    страницу авторизации Pet Friends, логинится на сайте, после выполнея основного кода закрывает браузер'''
    pytest.driver = webdriver.Chrome('C:/1/chromedriver.exe')
    pytest.driver.set_window_size(1280, 960)
    pytest.driver.implicitly_wait(10)
    yield
    pytest.driver.quit()

def test_petfriends():
    # Открыть базовую страницу PetFriends:
    pytest.driver.get("https://petfriends1.herokuapp.com/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Клик на кнопку "Зарегистрироваться"
    btn_new_user = pytest.driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()

    # Клик на ссылку "У меня уже есть аккаунт"
    btn_exist_acc = pytest.driver.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # Ввод email
    field_email = pytest.driver.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys(valid_email)

    # Ввод пароля
    field_pass = pytest.driver.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # Клик на кнопке "Войти"
    btn_submit = pytest.driver.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    assert  pytest.driver.current_url == 'https://petfriends1.herokuapp.com/all_pets',"login error"