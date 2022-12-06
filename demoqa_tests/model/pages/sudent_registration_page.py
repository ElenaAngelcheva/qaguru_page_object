from selene.support.shared import browser
from selene import have, command
from demoqa_tests.model import utils
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.tegs_input import TagsInput


class StudentRegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value):
        gender = {
            'Male': '[for=gender-radio-1]',
            'Female': '[for=gender-radio-2]',
            'Other': '[for=gender-radio-3]'
        }
        browser.element(gender[value]).click()
        return self

    def set_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def set_birth_day(self, birth_year, birth_month, birth_day):
        date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
        date_of_birth.select_year(birth_year)
        date_of_birth.select_month(birth_month)
        date_of_birth.select_day(birth_day)
        return self

    def set_subjects(self, values: list):
        for value in values:
            TagsInput(browser.element('#subjectsInput')).add(value)
        return self

    def set_hobbies(self, values: list):
        hobbies = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in values:
            browser.element(hobbies[value]).click()
        return self

    def set_picture(self, value):
        browser.element('#uploadPicture').send_keys(utils.upload_source(value))
        return self

    def set_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value):
        Dropdown(browser.element('#state')).autocomplete(option=value)
        return self

    def set_city(self, value):
        Dropdown(browser.element('#city')).autocomplete(option=value)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)






