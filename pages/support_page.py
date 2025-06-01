import time
import json
from elements.support_elements import Element_support, Element_expand_section, \
                                      Element_faq_table, Element_faq_table_rows, Element_specific_faq, \
                                      Element_expand_faq, Element_faq_category_table, Element_faq_question, \
                                      Element_faq_anwser, Element_send_support_request_button, \
                                      Element_support_request_text, Element_faq_category_back_button, \
                                      Element_submit_support_request, Element_support_confirm_message, \
                                      Element_support_confirm_button, Element_get_started_expand, Element_faq_answer_last_row , \
                                      Element_get_started_table, Element_get_started_table_rows, \
                                      Element_get_started_row_help_text, Element_present_overview_video, \
                                      Element_present_video_layout, Element_send_support_request_at_top, \
                                      Element_protip_checkbox
from pages.actions import mouse_click
from utilities.utils import normalize_text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SupportPage:
    def __init__(self, sb):
        self.sb = sb
        self.mouse_click = mouse_click

    def navigate_to_support_page(self):
        self.sb.click(f"{Element_support}")

    def navigate_to_specific_faq(self, faq_category_name):
        updated_element = Element_specific_faq % faq_category_name
        self.sb.click(f"{updated_element}")
        self.sb.click(f"{Element_expand_faq}")    

    def navigate_to_send_support_request(self):
        self.sb.scroll_to_bottom()
        self.sb.click(f"{Element_send_support_request_button}")

    def navigate_to_send_support_request_at_top(self):
        self.sb.click(f"{Element_send_support_request_at_top}")

    def go_back_to_faq_category(self):
        self.sb.click(f"{Element_faq_category_back_button}")

    def is_protip_enabled(self):
        print(self.sb.get_attribute(Element_protip_checkbox, "aria-checked"))
        return json.loads(str(self.sb.get_attribute(Element_protip_checkbox, "aria-checked")).lower())

    def submit_support_request(self):
        self.sb.click(f"{Element_submit_support_request}")

    def support_submit_completion(self):
        self.sb.click(f"{Element_support_confirm_button}")

    def expand_support_section(self, section):
        updated_element = Element_expand_section % section
        self.sb.wait_for_element_visible(f"{updated_element}", timeout=10)
        self.sb.hover(f"{updated_element}")
        self.mouse_click(self.sb, f"{updated_element}")

    def get_faq_categories(self):
        row_list = []
        self.sb.scroll_to_bottom()
        self.sb.wait_for_ready_state_complete()
        rows = self.sb.find_elements(f"{Element_faq_table}")
        for row in range(len(rows)):
            updated_element = Element_faq_table_rows % (row+1)
            row_list.append(self.sb.get_text(f"{updated_element}"))
        return row_list
    
    def get_get_started_categories(self):
        row_list = []
        self.sb.scroll_to_bottom()
        self.sb.wait_for_ready_state_complete()
        rows = self.sb.find_elements(f"{Element_get_started_table}")
        for row in range(len(rows)):
            updated_element = Element_get_started_table_rows % (row+1)
            row_list.append(self.sb.get_text(f"{updated_element}"))
            self.sb.slow_scroll_to(updated_element)
        return row_list

    def get_all_faq_question_answers(self):
        question_answer_map = {}
        rows = self.sb.find_elements(f"{Element_faq_category_table}")
        for row in range(len(rows)):
            Element_faq_question_updated = Element_faq_question % (row+1)
            faq_question = self.sb.get_text(f"{Element_faq_question_updated}")
            if row+1 == len(rows):
                Element_faq_anwser_updated = Element_faq_answer_last_row % (row+1)
            else:    
                Element_faq_anwser_updated = Element_faq_anwser % (row+1)
            faq_anwser = self.sb.get_text(f"{Element_faq_anwser_updated}")
            question_answer_map.update({normalize_text(faq_question): normalize_text(faq_anwser)})
        return question_answer_map

    def get_all_get_started_text(self):
        text_map = {}
        rows = self.sb.find_elements(f"{Element_get_started_table}")
        for row in range(len(rows)):
            updated_element = Element_get_started_table_rows % (row+1)
            category_name = self.sb.get_text(f"{updated_element}")
            updated_element = Element_get_started_row_help_text % (row+1)
            help_text = self.sb.get_text(f"{updated_element}")
            text_map.update({normalize_text(category_name): normalize_text(help_text)})
        return text_map

    def get_support_confirmation_message(self):
        return normalize_text(self.sb.get_text(f"{Element_support_confirm_message}"))

    def enter_message_for_support(self, message):
        self.sb.type(f"{Element_support_request_text}", message)

    def play_prezent_video(self):
        video_selector = f"{Element_present_overview_video}"
        # Wait for the video element to load (adjust selector if needed)
        self.sb.wait_for_element(video_selector)

        # Find the element with Selenium
        video_element = self.sb.driver.find_element(By.XPATH, video_selector)
        video_element.click()
        time.sleep(20)
        WebDriverWait(self.sb.driver, 240).until(
            EC.invisibility_of_element_located((By.XPATH, Element_present_video_layout))
        )

    def enable_pro_tip(self):
        self.sb.check_if_unchecked(Element_protip_checkbox)

    def disable_pro_tip(self):
        self.sb.uncheck_if_checked(Element_protip_checkbox)      