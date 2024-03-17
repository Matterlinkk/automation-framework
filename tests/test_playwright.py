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
    page.goto("https://www.qa-practice.com/elements/input/email")

    page.get_by_placeholder("Submit me").click()

    page.get_by_placeholder("Submit me").fill("qweqwe")

    page.get_by_placeholder("Submit me").press("Enter")

    expect(page.get_by_text("Enter a valid email address.")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_email_field_positive(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/email")

    page.get_by_placeholder("Submit me").click()

    page.get_by_placeholder("Submit me").fill("qweqwe@gmail.com")

    page.get_by_placeholder("Submit me").press("Enter")

    expect(page.locator('#result')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_password_field_negative(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/passwd")

    page.get_by_placeholder("Submit me").click()

    page.get_by_placeholder("Submit me").fill("qwe")

    page.get_by_placeholder("Submit me").press("Enter")

    expect(page.get_by_text("Low password complexity")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.inputs
def test_password_field_positive(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/passwd")

    page.get_by_placeholder("Submit me").click()

    page.get_by_placeholder("Submit me").fill("Aqwe!512ok")

    page.get_by_placeholder("Submit me").press("Enter")

    expect(page.get_by_text("Aqwe!512ok")).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_simple_button(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')

    page.get_by_role('button', name='Click').dispatch_event('click')

    expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_looks_like_a_button(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/like_a_button')

    page.get_by_role('link', name='Click').dispatch_event('click')

    expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.buttons
def test_disabled_button(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')

    dropdown = page.locator('select[class="form-select"]')
    dropdown.select_option('Enabled')

    page.get_by_role('button', name='Submit').dispatch_event('click')

    expect(page.get_by_text('Submitted')).to_be_visible()


@pytest.mark.playwright
@pytest.mark.checkboxes
def test_single_checkbox(page: Page):
    page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    page.locator('label[class="form-check-label"]').dispatch_event('click')

    page.get_by_role('button', name='Submit').dispatch_event('click')

    expect(page.locator('p[id="result-text"]')).to_contain_text(expected='select me or not')


@pytest.mark.playwright
@pytest.mark.checkboxes
def test_checkboxes(page: Page):
    page.goto('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    page.locator('input[value="one"]').dispatch_event('click')

    page.locator('input[value="two"]').dispatch_event('click')

    page.locator('input[value="three"]').dispatch_event('click')

    page.get_by_role('button', name='Submit').dispatch_event('click')

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
    page.goto('https://www.qa-practice.com/elements/select/single_select')

    dropdown = page.locator('select[class="form-select"]')

    dropdown.select_option(marker)

    page.locator('input[class="btn btn-primary"]').dispatch_event('click')

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

    page.goto('https://www.qa-practice.com/elements/select/mult_select')

    dropdown1 = page.locator('select[name="choose_the_place_you_want_to_go"]')
    dropdown2 = page.locator('select[name="choose_how_you_want_to_get_there"]')
    dropdown3 = page.locator('select[name="choose_when_you_want_to_go"]')

    dropdown1.select_option(marker_1)
    dropdown2.select_option(marker_2)
    dropdown3.select_option(marker_3)

    page.get_by_role('button', name='Submit').dispatch_event('click')

    result_text = page.locator('p[class="result-text"]').text_content()

    assert "to go by {} to the {} {}".format(marker_2, marker_1, marker_3).lower() == result_text


@pytest.mark.playwright
@pytest.mark.newtabs
def test_new_tab_link(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/link")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="New page will be opened on a").click()
    page1 = page1_info.value

    expect(page1.locator('p[class="result-text"]')).to_contain_text('I am a new page in a new tab')


@pytest.mark.playwright
@pytest.mark.newtabs
def test_new_tab_link_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Click").click()
    page1 = page1_info.value

    expect(page1.locator('p[class="result-text"]')).to_contain_text('I am a new page in a new tab')


@pytest.mark.playwright
@pytest.mark.textareas
def test_area_inputs(page: Page):
    value = 'playwright-pytest'

    page.goto('https://www.qa-practice.com/elements/textarea/single')

    page.locator('textarea[class="textarea form-control"]').fill(value)

    page.get_by_role('button', name='Submit').dispatch_event('click')

    expect(page.get_by_text(value)).to_be_visible()


@pytest.mark.playwright
@pytest.mark.textareas
def test_mult_area_inputs(page: Page):
    value1, value2, value3 = 'Q', "W", 'E'

    page.goto('https://www.qa-practice.com/elements/textarea/textareas')

    page.locator('textarea[name="first_chapter"]').fill(value1)

    page.locator('textarea[name="second_chapter"]').fill(value2)

    page.locator('textarea[name="third_chapter"]').fill(value3)

    page.get_by_role('button', name='Submit').dispatch_event('click')

    expect(page.locator('div[id="result"]')).to_contain_text('{}{}{}'.format(value1, value2, value3))


@pytest.mark.playwright
@pytest.mark.alerts
def test_confirmation_box_positive(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')

    page.on('dialog', lambda dialog: dialog.accept())

    page.get_by_role("link", name="Click").dispatch_event('click')

    expect(page.locator('div[id="result"]')).to_contain_text('Ok')


@pytest.mark.playwright
@pytest.mark.alerts
def test_confirmation_box_negative(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')

    page.on('dialog', lambda dialog: dialog.dismiss())

    page.get_by_role("link", name="Click").dispatch_event('click')

    expect(page.locator('div[id="result"]')).to_contain_text('Cancel')


@pytest.mark.playwright
@pytest.mark.alerts
def test_prompt_box_negative(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/prompt#')

    page.on('dialog', lambda dialog: dialog.dismiss())

    page.get_by_role("link", name="Click").dispatch_event('click')

    expect(page.locator('div[id="result"]')).to_contain_text('You canceled the prompt')


@pytest.mark.playwright
@pytest.mark.alerts
def test_prompt_box_positive(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/prompt#')

    value = 'qwerty'

    page.on('dialog', lambda dialog: dialog.accept(value))

    page.get_by_role("link", name="Click").dispatch_event('click')

    expect(page.locator('div[id="result"]')).to_contain_text(value)


@pytest.mark.playwright
@pytest.mark.dragndrops
def test_drag_n_drop_boxes(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')

    page.drag_and_drop(
        'div[class="rect-draggable ui-draggable ui-draggable-handle"]',
        'div[class="rect-droppable ui-droppable"]')

    expect(page.locator('p[class="ui-droppable"]')).to_contain_text('Dropped!')


@pytest.mark.playwright
@pytest.mark.dragndrops
def test_drag_n_drop_images(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/images')

    page.drag_and_drop(
        'img[class="rect-draggable ui-draggable ui-draggable-handle"]',
        'div[class="rect-droppable ui-droppable"]')

    expect(page.locator('div'
                        '[class="rect-droppable ui-droppable ui-state-highlight"]')).to_contain_text('Dropped!')


@pytest.mark.playwright
@pytest.mark.popups
def test_modal_pop_up_positive(page: Page):
    page.goto('https://www.qa-practice.com/elements/popup/modal')

    page.locator('button[data-bs-target="#exampleModal"]').click()

    page.locator('input[class="form-check-input"]').click()

    page.locator('button[form="id-checkbox-form"]').click()

    expect(page.locator('p[class="result-text"]')).to_contain_text('select me or not')


@pytest.mark.playwright
@pytest.mark.popups
def test_modal_pop_up_negative(page: Page):
    page.goto('https://www.qa-practice.com/elements/popup/modal')

    page.locator('button[data-bs-target="#exampleModal"]').click()

    page.locator('button[form="id-checkbox-form"]').click()

    expect(page.locator('p[class="result-text"]')).to_contain_text('None')


@pytest.mark.playwright
@pytest.mark.popups
def test_iframe_pop_up(page: Page):
    page.goto('https://www.qa-practice.com/elements/popup/iframe_popup')

    page.locator('button[data-bs-target="#exampleModal"]').click()

    text_to_input = page.frame_locator("iframe").get_by_text("I am the text you want to copy").text_content()

    page.get_by_role("button", name="Check").dispatch_event('click')

    page.locator('input[class="textinput textInput form-control"]').fill(text_to_input)

    page.locator('input[id="submit-id-submit"]').dispatch_event('click')

    expect(page.locator('div[class="alert alert-success"]')).to_contain_text('Correct!')


@pytest.mark.playwright
def test_add_remove_elements(page: Page):
    page.goto('https://the-internet.herokuapp.com/add_remove_elements/')

    page.get_by_text('Add Element').click(click_count=10)

    delete_buttons = page.get_by_text('Delete')

    for button in range(len(delete_buttons.all())):
        page.locator("//button[@class='added-manually'][1]").click()

    assert len(page.get_by_text('Delete').all()) == 0


@pytest.mark.playwright
def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    page.drag_and_drop('//div[@class="column"][1]', '//div[@class="column"][2]')

    expect(page.locator('//div[@class="column"][1]//header')).to_contain_text('B')


@pytest.mark.playwright
def test_dynamic_id(page: Page):
    pages = ['', '', '']

    for i in range(3):
        page.goto('http://uitestingplayground.com/dynamicid')

        pages[i] = page.locator('//div[@class="container"]//button').text_content()

    assert pages[0] == pages[1] == pages[2]


@pytest.mark.playwright
def test_class_attribute(page: Page):
    pages = ['', '', '']

    for i in range(3):
        page.goto('http://uitestingplayground.com/classattr')

        pages[i] = page.locator("//button[contains(text(), 'Button')][3]").text_content()

    assert pages[0] == pages[1] == pages[2]


@pytest.mark.playwright
def test_load_delay(page: Page):
    page.goto('http://uitestingplayground.com/')

    page.get_by_role('link', name='Load Delay').click()

    expect(page.locator("//button[@class='btn btn-primary']")).to_be_visible()


@pytest.mark.playwright
def test_ajax_data(page: Page):
    page.goto('http://uitestingplayground.com/')

    page.get_by_role('link', name='AJAX Data').click()

    page.get_by_role('button', name="Button Triggering AJAX Request").click()

    expect(page.locator('//p[@class="bg-success"]')).to_be_visible(timeout=20000)


@pytest.mark.playwright
def test_client_side_delay(page: Page):
    page.goto('http://uitestingplayground.com/')

    page.get_by_role('link', name='Client Side Delay').click()

    page.get_by_role('button', name="Button Triggering Client Side Logic").click()

    expect(page.locator('//p[@class="bg-success"]')).to_be_visible(timeout=20000)


@pytest.mark.playwright
def test_click(page: Page):
    page.goto('http://uitestingplayground.com/')

    page.get_by_role('link', name='Click').click()

    page.get_by_role('button', name="Button That Ignores DOM Click Event").click()

    expect(page.get_by_role('button', name="Button That Ignores DOM Click Event")).to_have_css('background-color',
                                                                                               'rgb(33, 136, 56)')


@pytest.mark.playwright
def test_text_input(page: Page):
    page.goto('http://uitestingplayground.com/textinput')

    value = 'qwe'

    page.get_by_placeholder('MyButton').fill(value)

    page.locator('//button[@id="updatingButton"]').click()

    expect(page.locator('//button[@id="updatingButton"]')).to_contain_text(value)


@pytest.mark.playwright
def test_scrollbar(page: Page):
    page.goto('http://uitestingplayground.com/scrollbars')

    page.locator('//button[@id="hidingButton"]').click()

    expect(page.locator('//button[@id="hidingButton"]')).to_be_visible()


@pytest.mark.playwright
def test_dynamic_test(page: Page):
    page.goto('http://uitestingplayground.com/dynamictable')

    def search_index(marker):
        for i in range(1, 5):
            row = page.locator('//div[@role="rowgroup"][2]//div[@role="row"][{}]'.format(i)).all()
            for j in range(len(row)):
                if marker in row[j].text_content():
                    if '%' in row[j].text_content():
                        return row[j].text_content()

    percent = search_index('Chrome')

    chrome_percent = page.locator('//p[@class="bg-warning"]').text_content()

    assert chrome_percent[12:] in percent


@pytest.mark.playwright
def test_verify_text(page: Page):
    page.goto('http://uitestingplayground.com/progressbar')

    page.get_by_role('button', name='Start').click()

    while '75%' not in page.locator('#progressBar').text_content():
        pass

    page.get_by_role('button', name='Stop').click()

    expect(page.locator('//p[@id="result"]')).to_contain_text('Result: 0')