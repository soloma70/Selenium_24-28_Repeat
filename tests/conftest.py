import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='session')
def driver_setup():
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''
    pytest.driver = webdriver.Chrome('C:/1/chromedriver.exe')
    pytest.driver.set_window_size(1280, 960)
    pytest.driver.implicitly_wait(5)
    yield pytest.driver
    pytest.driver.quit()
