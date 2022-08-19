from selene.support.shared import browser
from selene import have, command
from demoqa_tests import utils
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tegs_input import TagsInput


gender_mail = browser.element('[for="gender-radio-1"]')
sports_hobby = browser.element('[for="hobbies-checkbox-1"]')
reading_hobby = browser.element('[for="hobbies-checkbox-2"]')
music_hobby = browser.element('[for="hobbies-checkbox-3"]')


def given_opened_text_box():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').should(
        have.size_greater_than_or_equal(2)).perform(command.js.remove)


def test_register_student():
    #WHEN
    given_opened_text_box()

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov@bk.ru')

    gender_mail.click()

    browser.element('#userNumber').type('8999999999')

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.select_year(1999)
    date_of_birth.select_month(8)
    date_of_birth.select_day(9)

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Arts')
    subjects.add('History')
    subjects.add('Acc', autocomplete='Accounting')
    subjects.add('Phy', autocomplete='Physics')

    sports_hobby.click()
    reading_hobby.click()
    music_hobby.click()

    browser.element('#uploadPicture').send_keys(utils.upload_source('picture.jpg'))

    browser.element('#currentAddress').type('test')

    states = Dropdown(browser.element('#state'))
    states.autocomplete(option='Rajasthan')

    cityes = Dropdown(browser.element('#city'))
    cityes.autocomplete(option='Jaipur')

    browser.element('#submit').perform(command.js.scroll_into_view).click()


    #THEN
    results = Table(browser.element('.modal-dialog'))
    results.cells_of_row(0).should(have.exact_texts('Student Name', 'Ivan Ivanov'))
    results.cells_of_row(1).should(have.exact_texts('Student Email', 'ivanov@bk.ru'))
    results.cells_of_row(2).should(have.exact_texts('Gender', 'Male'))
    results.cells_of_row(3).should(have.exact_texts('Mobile', '8999999999'))
    results.cells_of_row(4).should(have.exact_texts('Date of Birth', '09 September,1999'))
    results.cells_of_row(5).should(have.exact_texts('Subjects', 'Arts, History, Accounting, Physics'))
    results.cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports, Reading, Music'))
    results.cells_of_row(7).should(have.exact_texts('Picture', 'picture.jpg'))
    results.cells_of_row(8).should(have.exact_texts('Address', 'test'))
    results.cells_of_row(9).should(have.exact_texts('State and City', 'Rajasthan Jaipur'))


