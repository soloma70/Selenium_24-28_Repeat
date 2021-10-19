from pages.auth_page import AuthPage
from settings import valid_email, valid_password
import time, pytest


def test_auth_page_with_valid_data():
    page = AuthPage(pytest.driver)
    time.sleep(1)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', 'Login error'

    time.sleep(2)
