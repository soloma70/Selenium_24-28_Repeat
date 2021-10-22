from pages.petfrinds import MainPage
import pytest, time

def test_petfriends_cookies(driver_setup):
    page = MainPage(driver_setup)
    page.scroll_down()
    time.sleep(3)