from selenium import webdriver
from pages.auth_page import AuthPage
from settings import valid_email, valid_password
import time, pytest

@pytest.fixture(autouse=True)
def driver_setup():
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает явные, страницу авторизации Pet Friends,
    логинится на сайте, после выполнея основного кода закрывает браузер'''
    pytest.driver = webdriver.Chrome('C:/1/chromedriver.exe')
    pytest.driver.set_window_size(1280, 960)
    pytest.driver.implicitly_wait(5)
    yield
    pytest.driver.quit()


def test_auth_page_with_valid_data():
    page = AuthPage(pytest.driver)
    time.sleep(3)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', 'Login error'

    time.sleep(3)
