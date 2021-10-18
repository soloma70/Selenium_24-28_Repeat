# pytest -v --driver Chrome --driver-path C:/1/chromedriver test_selenium_petfriends.py

from settings import valid_email, valid_password
import time


def test_petfriends(selenium):
    # Открыть базовую страницу PetFriends:
    selenium.get("https://petfriends1.herokuapp.com/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Клик на кнопку "Зарегистрироваться"
    btn_new_user = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()

    # Клик на ссылку "У меня уже есть аккаунт"
    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # Ввод email
    field_email = selenium.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys(valid_email)

    # Ввод пароля
    field_pass = selenium.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    # Клик на кнопке "Войти"
    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        # Сделать скриншот окна браузера:
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")