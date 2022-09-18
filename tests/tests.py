from demoqa_tests.model.application_manager import app
from demoqa_tests.model.date import User


student = User(
    first_name='Ivan',
    last_name= 'Ivanov',
    email='ivanov@bk.ru',
    gender='Male',
    mobile_number='8999999999',
    birth_year=1999,
    birth_month=8,
    birth_day=11,
    subject=['Arts', 'Hindi', 'Economics'],
    hobbi=['Sports', 'Reading', 'Music'],
    photo='picture.jpg',
    current_address='test',
    state='Rajasthan',
    city='Jaipur',
)


def test_register_student():
    #Given
    app.registration_form.open()
    #When
    app.registration_form.set_first_name(student.first_name)
    app.registration_form.set_last_name(student.last_name)
    app.registration_form.set_email(student.email)
    app.registration_form.set_gender(student.gender)
    app.registration_form.set_mobile_number(student.mobile_number)
    app.registration_form.set_birth_day(student.birth_year, student.birth_month, student.birth_day)
    app.registration_form.set_subjects(student.subject)
    app.registration_form.set_hobbies(student.hobbi)
    app.registration_form.set_picture(student.photo)
    app.registration_form.set_address(student.current_address)
    app.registration_form.set_state(student.state)
    app.registration_form.set_city(student.city)
    app.registration_form.submit()

    #Then
    app.resalt.sould_have_row_with_exact_texst(0, 'Student Name', student.full_name(student.first_name, student.last_name))
    app.resalt.sould_have_row_with_exact_texst(1, 'Student Email', student.email)
    app.resalt.sould_have_row_with_exact_texst(2, 'Gender', student.gender)
    app.resalt.sould_have_row_with_exact_texst(3, 'Mobile', student.mobile_number)
    app.resalt.sould_have_row_with_exact_texst(4, 'Date of Birth', student.birth_day_and_month(student.birth_day, student.birth_month, student.birth_year))
    app.resalt.sould_have_row_with_exact_texst(5, 'Subjects', student.subjects(student.subject))
    app.resalt.sould_have_row_with_exact_texst(6, 'Hobbies', student.hobbies(student.hobbi))
    app.resalt.sould_have_row_with_exact_texst(7, 'Picture', student.photo)
    app.resalt.sould_have_row_with_exact_texst(8, 'Address', student.current_address)
    app.resalt.sould_have_row_with_exact_texst(9, 'State and City', student.state_and_city(student.state, student.city))
