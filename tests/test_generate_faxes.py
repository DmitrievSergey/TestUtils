import os
from src.page_objects.LoginPage import LoginPage
from src.page_objects.SendFaxPage import SendFaxPage
from dotenv import load_dotenv

load_dotenv()


def test_generate_faxes(browser):
    LoginPage(browser) \
        .login_in(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    SendFaxPage(browser) \
        .validate_page_opened() \
        .send_fax()
