import time

from selene import command
from selene.support.conditions import have
from selene.support.shared import browser

LOGIN = ''
PASSWORD = ''


def up_the_resume():

    browser.open('https://hh.ru')
    browser.element('[data-qa="login"]').click()
    browser.element('[data-qa="expand-login-by-password"]').click()
    browser.element('[data-qa="login-input-username"]').send_keys(LOGIN)
    browser.element('[data-qa="login-input-password"]').send_keys(PASSWORD)
    browser.element('[data-qa="account-login-submit"]').click()
    browser.element('[data-qa="mainmenu_myResumes"]').click()

    resume = browser.element('span.b-marker').should(have.exact_text("QA Engineer / QA Automation (Python)"))
    resume.click()

    update_button = browser.element('[data-qa="resume-update-button"]')
    update_button.click()

# Repeat function's run
if __name__ == "__main__":
    while True:
        try:
            up_the_resume()
            print("Success! Resume is update!")
            browser.close()
            time.sleep(14401)

        except:
            print("OMG! Fail... Something is broken or Update-button already pushed.")
            browser.close()
            time.sleep(14401)
