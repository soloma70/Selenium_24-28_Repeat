from .base_page import BasePage
import os, pickle, pytest

class MainPage(BasePage):
    def __init__(self, driver, url='', timeout=10):
        if url == '':
            url = os.getenv('MAIN_URL') or 'https://petfriends1.herokuapp.com/'
        super().__init__(driver, url, timeout)
        with open('../tests/cookies_PF.txt', 'rb') as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()