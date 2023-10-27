import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_ENTER_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]""")
    LOCATOR_CONTACT_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_ENTER_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_ENTER_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_ENTER_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_SUBMIT_CONTACT_BTN = (By.CSS_SELECTOR, "button")


class OperationHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element '{TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}'")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element '{TestSearchLocators.LOCATOR_PASS_FIELD[1]}'")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_contact_name(self, word):
        logging.info(f"Send '{word}' to element '{TestSearchLocators.LOCATOR_ENTER_CONTACT_NAME[1]}'")
        contact_name_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_CONTACT_NAME)
        contact_name_field.clear()
        contact_name_field.send_keys(word)

    def enter_contact_email(self, word):
        logging.info(f"Send '{word}' to element '{TestSearchLocators.LOCATOR_ENTER_CONTACT_EMAIL[1]}'")
        contact_email_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_CONTACT_EMAIL)
        contact_email_field.clear()
        contact_email_field.send_keys(word)

    def enter_contact_content(self, word):
        logging.info(f"Send '{word}' to element '{TestSearchLocators.LOCATOR_ENTER_CONTACT_CONTENT[1]}'")
        contact_content_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_CONTACT_CONTENT)
        contact_content_field.clear()
        contact_content_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_contact_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        logging.info("Click contact button")
        time.sleep(3)

    def click_submit_contact_button(self):
        self.find_element(TestSearchLocators.LOCATOR_SUBMIT_CONTACT_BTN).click()
        logging.info("Click submit contact button")
        time.sleep(3)

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text '{text}' in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_enter_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_FIELD, time=3)
        text = enter_field.text
        logging.info(f"We find text '{text}' in enter field {TestSearchLocators.LOCATOR_ENTER_FIELD[1]}")
        return text

    def get_contact_text(self):
        contact_text = self.find_element(TestSearchLocators.LOCATOR_CONTACT_TEXT, time=3)
        text = contact_text.text
        logging.info(f"We find text '{text}' in contact field {TestSearchLocators.LOCATOR_CONTACT_TEXT[1]}")
        return text

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text


