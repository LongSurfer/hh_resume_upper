import os
import time
import allure
from selene.support.conditions import have


login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

def test_up_the_resume(setup_browser):
    browser = setup_browser

    with allure.step('Enter with password'):
        browser.open('https://hh.ru/account/login')
        browser.element('[data-qa="expand-login-by-password"]').click()
        browser.element('[data-qa="login-input-username"]').send_keys(f'{login}')
        browser.element('[data-qa="login-input-password"]').send_keys(f'{password}')
        browser.element('[data-qa="account-login-submit"]').click()
    with allure.step('Choose the resume'):
        browser.element('[data-qa="mainmenu_myResumes"]').click()

        resume = browser.element('span.b-marker').should(have.exact_text("QA Engineer / QA Automation (Python)"))
        resume.click()
    with allure.step('Update resume'):
        update_button = browser.element('[data-qa="resume-update-button"]')
        update_button.click()

    # attach.add_screenshot(browser)
    # attach.add_html(browser)
    # attach.add_logs(browser)

# Repite update:
if __name__ == "__main__":
    while True:
        try:
            test_up_the_resume()
            print("Success! Resume is update!")
            time.sleep(14401)

        except:
            print("Fail... Something is broken or Update-button already pushed.")
            time.sleep(14401)
