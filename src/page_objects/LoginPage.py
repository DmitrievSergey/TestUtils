from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class LoginPage(BasePage):
    PATH = '/'
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email-input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password-input")
    SIGNIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")

    def open_login_page(self):
        self._open_page(self.PATH)

    def input_login(self, login):
        self._input(self.USERNAME_INPUT, login)

    def input_pwd(self, password):
        self._input(self.PASSWORD_INPUT, password)

    def click_signin_button(self):
        self._click(self.SIGNIN_BUTTON)

    def login_in(self, login, password):
        self.open_login_page()
        self.input_login(login=login)
        self.input_pwd(password=password)
        self.click_signin_button()
