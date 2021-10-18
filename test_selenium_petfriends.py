# pytest -v --driver Chrome --driver-path C:/1/chromedriver test_selenium_petfriends.py

from settings import valid_email, valid_password
import time
import pytest
import uuid

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, driver):
    browser = driver
    browser.set_window_size(1400, 1000)
    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass  # just ignore any errors here


def test_petfriends(web_browser):
    # Открыть базовую страницу PetFriends:
    web_browser.get("https://petfriends1.herokuapp.com/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Клик на кнопку "Зарегистрироваться"
    btn_new_user = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()

    # Клик на ссылку "У меня уже есть аккаунт"
    btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # Ввод email
    field_email = web_browser.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys(valid_email)

    # Ввод пароля
    field_pass = web_browser.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # Клик на кнопке "Войти"
    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    if web_browser.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        # Сделать скриншот окна браузера:
        web_browser.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")