# pytest -v --driver Chrome --driver-path C:/1/chromedriver test_selenium_petfriends.py

import pytest
from selenium import webdriver
from settings import valid_email, valid_password
import time


@pytest.fixture(autouse=True)
def driver_setup():
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает явные, страницу авторизации Pet Friends,
    логинится на сайте, после выполнея основного кода закрывает браузер'''
    pytest.driver = webdriver.Chrome('C:/1/chromedriver.exe')
    pytest.driver.set_window_size(1280, 960)
    pytest.driver.implicitly_wait(10)
    # Открываем базовую страницу PetFriends:
    pytest.driver.get("https://petfriends1.herokuapp.com/")
    # Клик на кнопку "Зарегистрироваться"
    pytest.driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]").click()
    # Клик на ссылку "У меня уже есть аккаунт"
    pytest.driver.find_element_by_link_text(u"У меня уже есть аккаунт").click()
    yield
    pytest.driver.quit()

def test_show_petfriends():
    # Ввод email
    pytest.driver.find_element_by_id('email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)
    # Клик на кнопке "Войти"
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends", "login error"
