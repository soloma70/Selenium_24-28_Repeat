import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


# @pytest.fixture(autouse=True, scope='session')
# def web_driver():
#     '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
#     после выполнения основного кода закрывает браузер'''
#     web_driver = webdriver.Chrome('C:/1/chromedriver.exe')
#     web_driver.set_window_size(1280, 960)
#     web_driver.implicitly_wait(5)
#     yield web_driver
#     web_driver.quit()


@pytest.fixture(scope='session')
def web_driver():
    """Фикстура загружает страницу авторизации Pet Friends, логинится на сайте,
    после выполнения кода закрывает браузер"""
    web_driver = webdriver.Chrome('C:/1/chromedriver.exe')
    web_driver.set_window_size(1280, 960)
    web_driver.implicitly_wait(5)
    # Открываем базовую страницу PetFriends:
    web_driver.get("https://petfriends1.herokuapp.com/")
    # Клик на кнопку "Зарегистрироваться"
    web_driver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]").click()
    # Клик на ссылку "У меня уже есть аккаунт"
    web_driver.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт").click()
    # Ввод email
    web_driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Ввод пароля
    web_driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Клик на кнопке "Войти"
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    yield web_driver
    web_driver.quit()
