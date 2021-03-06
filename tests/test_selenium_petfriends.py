# pytest -v --driver Chrome --driver-path C:/1/chromedriver test_selenium_petfriends.py

from settings import valid_name


def test_login_pass(web_driver):
    """Тест проверяет загрузку страницы "Все питомцы" """
    # Проверка, что мы на главной странице
    assert web_driver.find_element_by_tag_name('h1').text == "PetFriends", "login error"


def test_show_all_pets(web_driver):
    """Тест проверяет наличие фото у питомца, наличие имени, возраста и породы"""
    # Получение массива данных из таблицы всех питомцев
    images_all_pets = web_driver.find_elements_by_css_selector('.card-deck.card-img-top')
    names_all_pets = web_driver.find_elements_by_css_selector('.card-deck.card-title')
    descriptions_all_pets = web_driver.find_elements_by_css_selector('.card-deck.card-text')
    # Внутри соответствующего масива есть имя питомца, возраст и вид
    for i in range(len(names_all_pets)):
        # Берём элемент с номером i (картинка для i-й карточки питомца). Каждая картинка имеет атрибут src, если была
        # загружена, и не имеет его, если отсутствует для данного питомца. Поэтому для проверки существования фотографии
        # в карточке мы просто проверяем, что путь, указанный в атрибуте src, не пустой.
        assert images_all_pets[i].get_attribute('src') != ''
        # Аналогичным образом поступаем с проверкой имени питомца. Берём i-го питомца и смотрим, что элемент, который
        # должен содержать его имя, имеет не пустой текст.
        assert names_all_pets[i].text != ''
        # Если текст есть, это не даёт гарантии, что в нём присутствует и вид питомца, и его возраст. Однако, если
        # текста нет совсем, то это точно ошибка. Это означает, что не выводится никакой текст.
        # Ищем в тексте этого элемента запятую, так как считаем её разделителем между этими двумя сущностями. Этого всё
        # ещё недостаточно, так как по отдельности ни возраст, ни вид питомца могут не отдаваться сервером (в этом
        # случае строка будет содержать только один символ ,)
        # Чтобы убедиться, что в строке есть и возраст питомца, и его вид, мы разделяем строку по запятой и ждём, что
        # каждая из частей разделённой строки будет длиной больше нуля. То есть в каждой части разделённого текста
        # присутствуют символы. Именно это и означает, что наша страница в карточке содержит и вид, и возраст питомца.
        assert descriptions_all_pets[i].text != ''
        assert ',' in descriptions_all_pets[i]
        parts_all_pets = descriptions_all_pets[i].text.split(',')
        assert len(parts_all_pets[0]) > 0
        assert len(parts_all_pets[1]) > 0


def test_show_my_pets(web_driver):
    """Тест проверяет загрузку страницы "Мои питомцы", наличие имени, возраста и породы; в статистике пользователя и в
    таблице одинаковае количество питомцев; хотя бы у половины питомцев есть фото; в таблице нет повторяющихся питомцев
    и повторяющихся имен питомцев"""
    # Переход на страницу "Мои питомцы"
    web_driver.find_element_by_xpath("//a[@href='/my_pets']").click()
    # Проверяем, что мы оказались на странице пользователя My Pets
    assert web_driver.find_element_by_tag_name('h2').text == valid_name
    # Получение массива данных из таблицы моих питомцев
    images_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr th img')
    names_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(1)')
    types_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(2)')
    ages_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(3)')
    # Получение количества питомцев из статистики пользователя
    count_my_pets = web_driver.find_element_by_css_selector('html body div div div').text.split('\n')
    count_my_pets_count = int((count_my_pets[1].split(' '))[1])
    # Объявление списка переменных и присваивание им пустых значений
    count_my_pets_name = 0
    count_my_pets_img = 0
    names_my_pets_mas = []
    types_my_pets_mas = []
    ages_my_pets_mas = []
    list_my_pets = []
    unique_list_my_pets = []
    # Перебор массива имен
    for j in range(len(names_my_pets)):
        count_my_pets_name += 1
        # Проверка фото питомца и обновление счетчика фото
        if images_my_pets[j].get_attribute('src') != '':
            count_my_pets_img += 1
        # Добавляем в списки имя, породу и возраст
        names_my_pets_mas += names_my_pets[j].text.split(", ")
        types_my_pets_mas += types_my_pets[j].text.split(", ")
        ages_my_pets_mas += ages_my_pets[j].text.split(", ")
        # Добавляем в список имя, породу и возраст
        list_my_pets.append([names_my_pets[j].text, types_my_pets[j].text, ages_my_pets[j].text])
        # Проверяем условие вхождения в список, если не входит - добавляем
        if list_my_pets[j] not in unique_list_my_pets:
            unique_list_my_pets.append(list_my_pets[j])
        # Проверяем, что у питомца j есть имя, возраст и порода (т.е.не пустые)
        assert names_my_pets[j].text != ''
        assert types_my_pets[j].text != ''
        assert ages_my_pets[j].text != ''

    # Присутствуют все питомцы
    assert count_my_pets_count == count_my_pets_name\
        , 'ERROR: В статистике пользователя и в таблице разное количество питомцев'
    # Хотя бы у половины питомцев есть фото
    assert count_my_pets_count / 2 <= count_my_pets_img, 'ERROR: Фото есть менее, чем у половины питомцев'
    # У всех питомцев разные имена
    assert len(names_my_pets_mas) == len(set(names_my_pets_mas)), 'ERROR: Есть повторяющиеся имена'
    # В списке нет повторяющихся питомцев
    assert len(list_my_pets) == len(unique_list_my_pets), 'ERROR: Есть повторяющиеся питомцы'


def test_exit(web_driver):
    """Тест проверяет работу кнопки "Выйти" """

    web_driver.find_element_by_xpath("//button[@class='btn btn-outline-secondary']").click()
    assert web_driver.find_element_by_xpath("//button[@class='btn btn-success']").text == 'Зарегистрироваться'\
        , 'ERROR: ошибка Log Out'
