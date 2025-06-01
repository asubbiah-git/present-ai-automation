from seleniumbase import BaseCase
from elements.login_elements import Element_username, Element_password, Element_continue, \
                                    Element_welcome_text, Element_slide_library
from elements.common_elements import Element_submit

class LoginPage:
    def __init__(self, sb):
        self.sb = sb

    def login(self, url, username, password):
        # Fill in login credentials
        self.sb.open(url)
        self.sb.type(Element_username, username)
        self.sb.wait_for_element_visible(Element_continue, timeout=10)
        self.sb.click(Element_continue)
        self.sb.type(Element_password, password)
        self.sb.click(Element_submit) 
        self.sb.wait_for_element_visible(f"{Element_welcome_text}", timeout=20)
        self.sb.click(f"{Element_slide_library}")
