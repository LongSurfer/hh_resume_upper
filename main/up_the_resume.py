import time
from selene.support.shared import browser

LOGIN = ''
PASSWORD = ''


def up_the_resume():
    browser.open('https://hh.ru')
    # Enter with password:
    browser.element('//*[@class="supernova-button"]').click()
    browser.element('//*[@data-qa="expand-login-by-password"]').click()
    browser.element('//*[@data-qa="login-input-username"]').send_keys(LOGIN)
    browser.element('//*[@data-qa="login-input-password"]').send_keys(PASSWORD)
    browser.element('//*[@data-qa="account-login-submit"]').click()
    # Choose the resume:
    browser.element('//*[@data-qa="mainmenu_myResumes"]').click()

    resume = browser.element('//*[contains(@class, "b-marker")][contains(.//text(), "QA Engineer / QA Automation (Python)")]')
    resume.click()
    # Update resume:
    update_button = browser.element('//*[@data-qa="resume-update-button"]')
    update_button.click()


if __name__ == "__main__":
    while True:
        try:
            up_the_resume()
            print("Success! Resume is update!")
            time.sleep(14401)

        except:
            print("Fail... Something is broken or Update-button already pushed.")
            time.sleep(14401)