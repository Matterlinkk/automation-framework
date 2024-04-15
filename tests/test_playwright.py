import allure
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.playwright
@pytest.mark.inputs
def test_input_field(page: Page):

    page.goto('https://www.qa-practice.com/elements/input/simple')

    input_field = page.get_by_placeholder('Submit me')

    input_field.dispatch_event('click')

    input_field.fill('ilovetea')

    page.keyboard.press('Enter')

    expect(page.locator('#result')).to_contain_text('ilovetea')


@pytest.mark.playwright
@pytest.mark.inputs
def test_email_field_negative(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/input/email")

    with allure.step('Click input field "Submit me"'):
        page.get_by_placeholder("Submit me").click()

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").fill("qweqwe")

        page.get_by_placeholder("Submit me").press("Enter")

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text("Enter a valid email address.")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_email_field_positive(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/input/email")

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").click()

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").fill("qweqwe@gmail.com")

        page.get_by_placeholder("Submit me").press("Enter")

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('#result')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_password_field_negative(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/input/passwd")

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").click()

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").fill("qwe")

        page.get_by_placeholder("Submit me").press("Enter")

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text("Low password complexity")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_password_field_positive(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/input/passwd")

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").click()

    with allure.step('Fill input field with text'):
        page.get_by_placeholder("Submit me").fill("Aqwe!512ok")

        page.get_by_placeholder("Submit me").press("Enter")

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text("Aqwe!512ok")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_simple_button(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/button/simple')

    with allure.step('Find button "Click" and click it'):
        page.get_by_role('button', name='Click').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_looks_like_a_button(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/button/like_a_button')

    with allure.step('Find button "Click" and click it'):
        page.get_by_role('link', name='Click').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_disabled_button(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/button/disabled')

    with allure.step('Find dropdown-list and select "Enable" option'):
        dropdown = page.locator('select[class="form-select"]')
        dropdown.select_option('Enabled')

    with allure.step('Find button "Submit" and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.checkboxes
def test_single_checkbox(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    with allure.step('Finc checkbox and click it'):
        page.locator('label[class="form-check-label"]').dispatch_event('click')

    with allure.step('Find button "Submit" and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('p[id="result-text"]')).to_contain_text(expected='select me or not')


@pytest.mark.playwright
@pytest.mark.checkboxes
def test_checkboxes(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    with allure.step('Find checkboxes and click all'):
        page.locator('input[value="one"]').dispatch_event('click')

        page.locator('input[value="two"]').dispatch_event('click')

        page.locator('input[value="three"]').dispatch_event('click')

    with allure.step('Find "Submit" button and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text('one, two, three')).to_be_visible()


# parametrize tests
@pytest.mark.parametrize(
    'marker',
    [
        'Python',
        'Ruby',
        'JavaScript',
        'Java',
        'C#'
    ]
)
@pytest.mark.playwright
@pytest.mark.selects
def test_single_select(page: Page, marker):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/select/single_select')

    with allure.step('Find dropdown-list and select value "{}"'.format(marker)):
        dropdown = page.locator('select[class="form-select"]')

        dropdown.select_option(marker)

    with allure.step('Find button "Submit" and click it'):
        page.locator('input[class="btn btn-primary"]').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('p[class="result-text"]')).to_contain_text(expected=marker)


def generate_pairs():
    you_want_to_go_list = ['Sea', 'Mountains', 'Old town', 'Ocean', 'Restaurant']
    you_want_to_get_there_list = ['Car', 'Bus', 'Train', 'Air']
    when_you_want_to_go_list = ['Today', 'Tomorrow', 'Next week']

    pair_list = []

    for you_want in you_want_to_go_list:
        for get_there in you_want_to_get_there_list:
            for when_you_want in when_you_want_to_go_list:
                pair_list.append(pytest.param((you_want, get_there, when_you_want),
                                              id='{}, {}, {}'.format(you_want, get_there, when_you_want)))

    return pair_list


# pairwise testing
@pytest.mark.parametrize(
    "pairs",
    generate_pairs()[:5]
)
@pytest.mark.playwright
@pytest.mark.selects
def test_mult_select(page: Page, pairs):
    marker_1, marker_2, marker_3 = pairs

    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/select/mult_select')

    with allure.step('Find dropdown-lists by locators'):
        dropdown1 = page.locator('select[name="choose_the_place_you_want_to_go"]')
        dropdown2 = page.locator('select[name="choose_how_you_want_to_get_there"]')
        dropdown3 = page.locator('select[name="choose_when_you_want_to_go"]')

    with allure.step('Select option for each dropdown-list'):
        dropdown1.select_option(marker_1)
        dropdown2.select_option(marker_2)
        dropdown3.select_option(marker_3)

    with allure.step('Find "Submit" button and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        result_text = page.locator('p[class="result-text"]').text_content()

        assert "to go by {} to the {} {}".format(marker_2, marker_1, marker_3).lower() == result_text


@pytest.mark.playwright
@pytest.mark.newtabs
def test_new_tab_link(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/new_tab/link")

    with allure.step('Open the page in a new tab'):
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="New page will be opened on a new tab").click()

    with allure.step('Go to the web page'):
        page1 = page1_info.value

        expect(page1.locator('p[class="result-text"]')).to_contain_text('I am a new page in a new tab')


@pytest.mark.playwright
@pytest.mark.newtabs
def test_new_tab_link_button(page: Page):
    with allure.step('Go to the web page'):
        page.goto("https://www.qa-practice.com/elements/new_tab/button")

    with allure.step('Open the page in a new tab'):
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="Click").click()

    with allure.step('Compare expected result and actual result'):
        page1 = page1_info.value

        expect(page1.locator('p[class="result-text"]')).to_contain_text('I am a new page in a new tab')


@pytest.mark.playwright
@pytest.mark.textareas
def test_area_inputs(page: Page):
    value = 'playwright-pytest'

    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/textarea/single')

    with allure.step('Find textarea and fill it with text'):
        page.locator('textarea[class="textarea form-control"]').fill(value)

    with allure.step('Find "Submit" button and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.get_by_text(value)).to_be_visible()


@pytest.mark.playwright
@pytest.mark.textareas
def test_mult_area_inputs(page: Page):
    value1, value2, value3 = 'Q', "W", 'E'

    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/textarea/textareas')

    with allure.step('Find textareas and fill values'):
        page.locator('textarea[name="first_chapter"]').fill(value1)

        page.locator('textarea[name="second_chapter"]').fill(value2)

        page.locator('textarea[name="third_chapter"]').fill(value3)

    with allure.step('Find "Submit" button and click it'):
        page.get_by_role('button', name='Submit').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[id="result"]')).to_contain_text('{}{}{}'.format(value1, value2, value3))


@pytest.mark.playwright
@pytest.mark.alerts
def test_confirmation_box_positive(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/alert/confirm#')

        page.on('dialog', lambda dialog: dialog.accept())

    with allure.step('Click button'):
        with allure.step('Accept modal window'):
            page.get_by_role("link", name="Click").dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[id="result"]')).to_contain_text('Ok')


@pytest.mark.playwright
@pytest.mark.alerts
def test_confirmation_box_negative(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/alert/confirm#')

    page.on('dialog', lambda dialog: dialog.dismiss())

    with allure.step('Click button'):
        with allure.step('Dismiss modal window'):
            page.get_by_role("link", name="Click").dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[id="result"]')).to_contain_text('Cancel')


@pytest.mark.playwright
@pytest.mark.alerts
def test_prompt_box_negative(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/alert/prompt#')

    page.on('dialog', lambda dialog: dialog.dismiss())

    with allure.step('Click button'):
        with allure.step('Dismiss modal window'):
            page.get_by_role("link", name="Click").dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[id="result"]')).to_contain_text('You canceled the prompt')


@pytest.mark.playwright
@pytest.mark.alerts
def test_prompt_box_positive(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/alert/prompt#')

    value = 'qwerty'

    page.on('dialog', lambda dialog: dialog.accept(value))

    with allure.step('Click button'):
        with allure.step('Accept modal window and fill input field'):
            page.get_by_role("link", name="Click").dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[id="result"]')).to_contain_text(value)


@pytest.mark.playwright
@pytest.mark.dragndrops
def test_drag_n_drop_boxes(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')

    with allure.step('Drag and drop to target field'):
        page.drag_and_drop(
            'div[class="rect-draggable ui-draggable ui-draggable-handle"]',
            'div[class="rect-droppable ui-droppable"]')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('p[class="ui-droppable"]')).to_contain_text('Dropped!')


@pytest.mark.playwright
@pytest.mark.dragndrops
def test_drag_n_drop_images(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/dragndrop/images')

    with allure.step('Drag and drop to target field'):
        page.drag_and_drop(
            'img[class="rect-draggable ui-draggable ui-draggable-handle"]',
            'div[class="rect-droppable ui-droppable"]')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div'
                            '[class="rect-droppable ui-droppable ui-state-highlight"]')).to_contain_text('Dropped!')


@pytest.mark.playwright
@pytest.mark.popups
def test_modal_pop_up_positive(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/popup/modal')

    with allure.step('Click "Launch Pop-Up" button'):
        page.locator('button[data-bs-target="#exampleModal"]').click()

    with allure.step('Find checkbox and click it'):
        page.locator('input[class="form-check-input"]').click()

    with allure.step('Find "Send" button and click it'):
        page.locator('button[form="id-checkbox-form"]').click()

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('p[class="result-text"]')).to_contain_text('select me or not')


@pytest.mark.playwright
@pytest.mark.popups
def test_modal_pop_up_negative(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/popup/modal')

    with allure.step('Click "Launch Pop-Up" button'):
        page.locator('button[data-bs-target="#exampleModal"]').click()

    with allure.step('Find "Send" button and click it'):
        page.locator('button[form="id-checkbox-form"]').click()

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('p[class="result-text"]')).to_contain_text('None')


@pytest.mark.playwright
@pytest.mark.popups
def test_iframe_pop_up(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://www.qa-practice.com/elements/popup/iframe_popup')

    with allure.step('Click "Launch Pop-Up" button'):
        page.locator('button[data-bs-target="#exampleModal"]').click()

    with allure.step('Copy text from iframe'):
        text_to_input = page.frame_locator("iframe").get_by_text("I am the text you want to copy").text_content()

    with allure.step('Find "Check" button and click it'):
        page.get_by_role("button", name="Check").dispatch_event('click')

    with allure.step('Find input-field and fill with text'):
        page.locator('input[class="textinput textInput form-control"]').fill(text_to_input)

    with allure.step('Find "Submit" button and click it'):
        page.locator('input[id="submit-id-submit"]').dispatch_event('click')

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('div[class="alert alert-success"]')).to_contain_text('Correct!')


@pytest.mark.playwright
def test_add_remove_elements(page: Page):
    with allure.step('Go to the web page'):
        page.goto('https://the-internet.herokuapp.com/add_remove_elements/')

    with allure.step('Create 10 elements'):
        page.get_by_text('Add Element').click(click_count=10)

    with allure.step('Delete 10 buttons'):
        delete_buttons = page.get_by_text('Delete')

        for button in range(len(delete_buttons.all())):
            page.locator("//button[@class='added-manually'][1]").click()

    with allure.step('Compare expected result and actual result'):
        assert len(page.get_by_text('Delete').all()) == 0


@pytest.mark.playwright
def test_example(page: Page) -> None:
    with allure.step('Go to the web page'):
        page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    with allure.step('Drag and drop to the target'):
        page.drag_and_drop('//div[@class="column"][1]', '//div[@class="column"][2]')

        expect(page.locator('//div[@class="column"][1]//header')).to_contain_text('B')


@pytest.mark.playwright
def test_dynamic_id(page: Page):
    pages = ['', '', '']

    with allure.step('Find button on the web page and write id'):
        for i in range(3):
            page.goto('http://uitestingplayground.com/dynamicid')

            pages[i] = page.locator('//div[@class="container"]//button').text_content()

    with allure.step('Compare button names with different IDs'):
        assert pages[0] == pages[1] == pages[2]


@pytest.mark.playwright
def test_load_delay(page: Page):
    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/')

    with allure.step('Click for start load delay'):
        page.get_by_role('link', name='Load Delay').click()

    with allure.step('Wait for visible element'):
        expect(page.locator("//button[@class='btn btn-primary']")).to_be_visible()


@pytest.mark.playwright
def test_ajax_data(page: Page):
    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/')

    with allure.step('Click button for trigger AJAX Request'):
        page.get_by_role('link', name='AJAX Data').click()

        page.get_by_role('button', name="Button Triggering AJAX Request").click()

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('//p[@class="bg-success"]')).to_be_visible(timeout=20000)


@pytest.mark.playwright
def test_client_side_delay(page: Page):
    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/')

        page.get_by_role('link', name='Client Side Delay').click()

    with allure.step('Click button for trigger Client Side Logic'):
        page.get_by_role('button', name="Button Triggering Client Side Logic").click()

    with allure.step('Wait for visible element'):
        expect(page.locator('//p[@class="bg-success"]')).to_be_visible(timeout=20000)


@pytest.mark.playwright
def test_click(page: Page):

    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/')

        page.get_by_role('link', name='Click').click()

    with allure.step('Click button'):
        page.get_by_role('button', name="Button That Ignores DOM Click Event").click()

    with allure.step("Compare buttons` color"):
        expect(page.get_by_role('button', name="Button That Ignores DOM Click Event")).to_have_css('background-color',
                                                                                                   'rgb(33, 136, 56)')


@pytest.mark.playwright
def test_text_input(page: Page):

    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/textinput')

    value = 'qwe'

    with allure.step('Find input-field and fill it by value "{}"'.format(value)):
        page.get_by_placeholder('MyButton').fill(value)

    with allure.step('Find button and click it'):
        page.locator('//button[@id="updatingButton"]').click()

    with allure.step('Compare expected result and actual result'):
        expect(page.locator('//button[@id="updatingButton"]')).to_contain_text(value)


@pytest.mark.playwright
def test_scrollbar(page: Page):

    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/scrollbars')

    with allure.step('Find button and click it'):
        page.locator('//button[@id="hidingButton"]').click()

    with allure.step('Wait for visible element'):
        expect(page.locator('//button[@id="hidingButton"]')).to_be_visible()


@pytest.mark.playwright
def test_dynamic_test(page: Page):

    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/dynamictable')

    def search_index(marker):
        for i in range(1, 5):
            row = page.locator('//div[@role="rowgroup"][2]//div[@role="row"][{}]'.format(i)).all()
            for j in range(len(row)):
                if marker in row[j].text_content():
                    if '%' in row[j].text_content():
                        return row[j].text_content()

    with allure.step('Find value by marker'):
        percent = search_index('Chrome')

        chrome_percent = page.locator('//p[@class="bg-warning"]').text_content()

    with allure.step('Compare expected result and actual result'):
        assert chrome_percent[12:] in percent


@pytest.mark.playwright
def test_verify_text(page: Page):

    with allure.step('Go to the web page'):
        page.goto('http://uitestingplayground.com/progressbar')

    with allure.step('Find button and start progressbar process'):
        page.get_by_role('button', name='Start').click()

    with allure.step('Wait for 75%'):
        while '75%' not in page.locator('#progressBar').text_content():
            pass

    with allure.step('Find button and stop progressbar process'):
        page.get_by_role('button', name='Stop').click()

    with allure.step('Compare expected result and actual result'):
        assert int(page.locator('//p[@id="result"]').text_content()[8:9]) <= 2
