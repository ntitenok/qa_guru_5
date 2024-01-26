from selene import browser, have, be
from selene import by
import os


def test_form_student_registration():
    # Предусловие. Перейти на страницу Регистрации формы для студента
    browser.open('/automation-practice-form')

    # Заполнить персональные данные студента
    browser.element('#firstName').should(be.blank).type('Nikolay')
    browser.element('#lastName').should(be.blank).type('Titenok')
    browser.element('#userEmail').should(be.blank).type('ntitenok@gmail.com')
    browser.element('[for="gender-radio-1').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    # Указать дату рождения

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1989')).click()
    browser.element('.react-datepicker__day--022').click()

    # Выбрать предметы

    browser.element('#subjectsInput').type('Computer')
    browser.element(by.text('Computer Science')).click()
    browser.element('#subjectsInput').type('Physics').press_enter()

    """ Указать хобби (А как можно сразу по несколькм чекбоксам кликнуть, например, по двум определенным? 
    Надо цикл использовать или есть функция у Селена?)"""

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Загрузить файл
    browser.element('#uploadPicture').send_keys(os.path.abspath('data\\myfile'))

    # Выбрать местожительство
    browser.element('#currentAddress').should(be.blank).type('Мой адрес — ни дом и не улица')

    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Panipat')).click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('Nikolay Titenok', 'ntitenok@gmail.com', 'Male', '1234567890', '22 May,1989',
                   'Computer Science, Physics', 'Sports, Reading, Music', 'myfile', 'Мой адрес — ни дом и не улица',
                   'Haryana Panipat'))
