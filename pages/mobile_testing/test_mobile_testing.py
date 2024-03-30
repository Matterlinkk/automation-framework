import allure
import pytest

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search_to(driver, url):
    with allure.step('Open the browser'):
        wait_for_chrome = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]'))
        )


        browser = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')
        browser.click()

    with allure.step('Wait for urlbar'):
        wait_for_urlbar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/search_box_text')))

        url_bar = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/search_box_text')
        url_bar.click()

    with allure.step('Fill url in url bar'):
        wait_for_urlbar_again = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.ID, 'com.android.chrome:id/url_bar')))

        url_bar_again = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/url_bar')

        url_bar_again.send_keys(url)

    with allure.step('Go to the webpage'):
        driver.press_keycode(66)

    return driver


def swap(driver):
    with allure.step('Scroll down the screen'):
        wait_for_from_el = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Image[@text="logo"]')))
        wait_for_to_el = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Pop-Up"]')))

        from_el = driver.find_element(AppiumBy.XPATH, '//android.widget.Image[@text="logo"]')
        to_el = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Pop-Up"]')

        driver.scroll(to_el, from_el)

        wait_for_req = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="req_header"]')))


@pytest.mark.appium
def test_looks_like_a_button(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/button/like_a_button')

    swap(driver)

    with allure.step('Click the button'):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Click"]').click()

        swap(driver)

        wait_for_req = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="req_header"]')))

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert "Submitted" == result_text


@pytest.mark.appium
def test_simple_button(driver_init):

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/button/simple')

    swap(driver)

    with allure.step('Click submit button'):
        button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'Submitted' == result_text


@pytest.mark.appium
def test_disabled_button(driver_init):

    driver = search_to(driver_init, 'https://www.qa-practice.com/')

    with allure.step('Click "Simple button" button'):
        wait_for_simple_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Simple button"]')))

        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Simple button"]').click()

    swap(driver)

    with allure.step('Click disabled button'):
        disabled_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Disabled"]')
        disabled_button.click()

    swap(driver)

    with allure.step('Change state to "Enabled"'):
        wait_for_states = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="id_select_state"]'))
        )

        states = driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="id_select_state"]')
        states.click()

        wait_for_enable_state = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Enabled"]'))
        )

        enable_state = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Enabled"]')
        enable_state.click()

    with allure.step('Click submit button'):
        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        wait_for_requirements = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]'))
        )

        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'Submitted' == result_text


@pytest.mark.appium
def test_text_input(driver_init):

    value = 'QWE'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/input/simple')

    swap(driver)

    with allure.step('Fill the input field with text'):
        input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_text_string"]')
        input.click()
        input.send_keys(value)
        driver.press_keycode(66)

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert value == result_text


@pytest.mark.appium
def test_email_input(driver_init):

    value = 'qwerty123@gmail.com'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/input/email')

    swap(driver)

    with allure.step('Fill the input field with text'):
        input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_email"]')
        input.click()
        input.send_keys(value)
        driver.press_keycode(66)

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert value == result_text


@pytest.mark.appium
def test_password_input(driver_init):

    value = 'QWE-sad213312'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/input/passwd')

    swap(driver)

    with allure.step('Fill the input field with text'):
        input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_password"]')
        input.click()
        input.send_keys(value)
        driver.press_keycode(66)

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert value == result_text


@pytest.mark.appium
def test_single_checkbox(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/checkbox/single_checkbox')

    swap(driver)

    with allure.step('Click checkbox'):
        checkbox = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="id_checkbox_0"]')
        checkbox.click()

        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'select me or not' == result_text


@pytest.mark.appium
def test_multi_checkboxes(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    swap(driver)

    with allure.step('Click checkboxes'):
        checkbox1 = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="id_checkboxes_0"]')
        checkbox2 = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="id_checkboxes_1"]')
        checkbox3 = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="id_checkboxes_2"]')

        checkbox1.click()
        checkbox2.click()
        checkbox3.click()

    with allure.step('Click submit button'):
        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)
    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'one, two, three' == result_text


@pytest.mark.parametrize(
    "value",
    ['Python', 'Ruby', 'JavaScript', 'Java', 'C#',]
)
@pytest.mark.appium
def test_single_select(driver_init, value):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/select/single_select')

    swap(driver)

    with allure.step('Select value "{}" `from` dropdown-list'):
        select = driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="id_choose_language"]')
        select.click()

        select_value = driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{}"]'.format(value))

        select_value.click()

    with allure.step('Click submit button'):
        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert value == result_text


@pytest.mark.appium
def test_multiply_selects(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/select/mult_select')

    swap(driver)

    with allure.step('Select values `from` dropdown-lists'):
        first_select = driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Spinner[@resource-id="id_choose_the_place_you_want_to_go"]')
        second_select = driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Spinner[@resource-id="id_choose_how_you_want_to_get_there"]')
        third_select = driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Spinner[@resource-id="id_choose_when_you_want_to_go"]')

        first_select.click()
        driver.find_element(AppiumBy.XPATH,
                            '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Restaurant"]').click()

        second_select.click()
        driver.find_element(AppiumBy.XPATH,
                            '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Bus"]').click()

        third_select.click()
        driver.find_element(AppiumBy.XPATH,
                            '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Next week"]').click()

    with allure.step('Click submit button'):
        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'to go by bus to the restaurant next week' == result_text


@pytest.mark.appium
def test_new_tab_link(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/new_tab/link')

    swap(driver)

    with allure.step('Open new page in new tab'):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="New page will be opened on a new tab"]').click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'I am a new page in a new tab' == result_text


@pytest.mark.appium
def test_new_tab_button(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/new_tab/button')

    swap(driver)

    with allure.step('Open new page in new tab'):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Click"]').click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'I am a new page in a new tab' == result_text


@pytest.mark.appium
def test_single_text_area(driver_init):
    value = 'qwe'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/textarea/single')

    swap(driver)

    with allure.step('Fill the input field with text'):
        input_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_text_area"]')
        input_field.send_keys(value)

        driver.press_keycode(66)

    with allure.step('Click button'):
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]').click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'qwe' == result_text


@pytest.mark.appium
def test_multiply_text_area(driver_init):
    def swap_to(driver, from_el, to_el, wait_el):
        with allure.step('Scroll down the screen'):
            wait_for_from_el = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(from_el))
            wait_for_to_el = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(to_el))

            from_el = driver.find_element(*from_el)
            to_el = driver.find_element(*to_el)

            driver.scroll(to_el, from_el)

            wait_for_second_chapter = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(wait_el))

    value_1 = 'Q'
    value_2 = 'W'
    value_3 = 'E'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/textarea/textareas')

    from_el_first = (AppiumBy.XPATH, '//android.widget.Image[@text="logo"]')
    to_el_first = (AppiumBy.XPATH, '//android.widget.TextView[@text="Pop-Up"]')
    wait_el_first = (AppiumBy.XPATH, '//android.view.View[@text="Second chapter"]')

    swap_to(driver, from_el_first, to_el_first, wait_el_first)

    first_area = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_first_chapter"]')
    first_area.send_keys(value_1)

    second_area = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_second_chapter"]')
    second_area.send_keys(value_2)

    from_el_second = (AppiumBy.XPATH, '//android.view.View[@text="First chapter*"]')
    to_el_second = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_second_chapter"]')
    wait_el_second = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="req_header"]')

    swap_to(driver, from_el_second, to_el_second, wait_el_second)

    third_area = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_third_chapter"]')
    third_area.send_keys(value_3)

    submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
    submit_button.click()

    from_el_first = (AppiumBy.XPATH, '//android.widget.Image[@text="logo"]')
    to_el_first = (AppiumBy.XPATH, '//android.widget.TextView[@text="Pop-Up"]')
    wait_el_first = (AppiumBy.XPATH, '//android.view.View[@text="Second chapter"]')

    swap_to(driver, from_el_first, to_el_first, wait_el_first)

    from_el_second = (AppiumBy.XPATH, '//android.view.View[@text="First chapter*"]')
    to_el_second = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_second_chapter"]')
    wait_el_second = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="req_header"]')

    swap_to(driver, from_el_second, to_el_second, wait_el_second)

    result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

    from_el_third = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="req_header"]')
    to_el_third = (AppiumBy.XPATH, '//android.view.View[@text="Third chapter"]')
    wait_el_third = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_first_chapter"]')

    swap_to(driver, from_el_third, to_el_third, wait_el_third)

    with allure.step('Compare actual result and expected result'):
        assert result_text == "{}\n{}\n{}".format(value_1, value_2, value_3)


@pytest.mark.appium
def test_alert_box(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/alert/alert')

    swap(driver)

    with allure.step('Click the button'):
        button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Click"]')
        button.click()

    wait_for_alert = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.android.chrome:id/button_bar"]'))
    )

    with allure.step('Click "Ok" in modal window'):
        ok_button = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.android.chrome:id/button_bar"]')
        ok_button.click()


@pytest.mark.appium
def test_confirmation_box(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/alert/confirm')

    swap(driver)

    with allure.step('Click the button'):
        button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Click"]')
        button.click()

    with allure.step('Accept modal window'):
        wait_for_alert = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.android.chrome:id/button_bar"]'))
        )

        ok_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]')
        ok_button.click()

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'Ok' == result_text


@pytest.mark.appium
def test_promt_box(driver_init):
    value = 'qwe'

    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/alert/prompt')

    swap(driver)

    with allure.step('Click the button'):
        button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Click"]')
        button.click()

    with allure.step('Fill input field with text'):
        input_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/js_modal_dialog_prompt"]')
        input_field.send_keys(value)

    with allure.step('Accept modal window'):
        ok_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]')
        ok_button.click()

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert value == result_text


@pytest.mark.appium
def test_modal_pop_up(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/popup/modal')

    swap(driver)

    with allure.step('Launch Pop-up'):
        launch_pop_up = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Launch Pop-Up"]')
        launch_pop_up.click()

    with allure.step('Click checkbox from pop-up'):
        wait_for_pop_up = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.app.Dialog[@resource-id="exampleModal"]/android.view.View/android.view.View'))
        )

        checkbox = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="id_checkbox_0"]')
        checkbox.click()

    with allure.step('Click send button'):
        send_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Send"]')
        send_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="result-text"]').text

        assert 'select me or not' == result_text


@pytest.mark.appium
def test_iframe_pop_up(driver_init):
    driver = search_to(driver_init, 'https://www.qa-practice.com/elements/popup/iframe_popup')

    swap(driver)

    with allure.step('Click launch pop-up'):
        launch_pop_up = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Launch Pop-Up"]')
        launch_pop_up.click()

        wait_for_pop_up = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (AppiumBy.XPATH, '//android.app.Dialog[@resource-id="exampleModal"]/android.view.View/android.view.View'))
        )

    with allure.step('Copy text for input field'):
        copy_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="text-to-copy"]').text

    with allure.step('Click check button'):
        check_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Check"]')
        check_button.click()

    swap(driver)

    with allure.step('Fill input field with coppied text'):
        input_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="id_text_from_iframe"]')
        input_field.send_keys(copy_text)

    with allure.step('Click submit button'):
        submit_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="submit-id-submit"]')
        submit_button.click()

    swap(driver)

    with allure.step('Compare actual result and expected result'):
        result_text = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="check-result"]').text

        assert 'Correct!' == result_text
