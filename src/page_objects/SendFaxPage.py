import time

from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class SendFaxPage(BasePage):
    PATH = '/sandbox'
    INBOUND_FAX_TAB = (By.XPATH, "//span[contains(text(),'Inbound Fax')]")
    USER_ICON = (By.CSS_SELECTOR, "i[class='fa fa-user']")
    RECIPIENT_INPUT = (By.XPATH, "//input[@type='text']")
    NUMBERS_LIST = (By.XPATH, "//div[@class='ng-dropdown-panel-items scroll-host']")
    SEND_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
    FAX_NUMBER_TEXT = (By.XPATH, "//label[contains(text(),'Fax Number')]")
    CP_LINK = (By.XPATH, "//span[contains(text(),'Cover Pages')]")

    def open_send_fax_page(self):
        self._open_page(self.PATH)

    def validate_page_opened(self):
        self._verify_element_presence(self.FAX_NUMBER_TEXT)
        return self

    def validate_element_presence(self):
        self._verify_element_presence(self.CP_LINK)
        return self

    def click_recipient_number(self):
        recipient_number = (
            By.XPATH, "//span[@class='ng-option-label ng-star-inserted'][contains(text(),'" + self.browser.fax_number + "')]")
        self._click(recipient_number)

    def input_recipient_number(self):
        self._input(self.RECIPIENT_INPUT, self.browser.fax_number)

    def click_send_button(self):
        self._click(self.SEND_BUTTON)

    def click_inbound_tab(self):
        self._click(self.INBOUND_FAX_TAB)

    def send_fax(self):
        self.open_send_fax_page()
        self.validate_element_presence()
        self.click_inbound_tab()
        for i in range(0, self.browser.fax_count, 1):
            self.input_recipient_number()
            self.click_recipient_number()
            self.click_send_button()
            time.sleep(15)
