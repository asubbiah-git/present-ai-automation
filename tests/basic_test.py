import time
import pytest
from collections import Counter
from seleniumbase import BaseCase
from pages.search import SearchInAPage
from pages.login_page import LoginPage
from pages.support_page import SupportPage
from utilities.utils import normalize_text
from utilities.common import suite_data, go_to_faq_section

@pytest.mark.usefixtures("login_credentials")
class TestDashboard(BaseCase):
    @suite_data("testdata/support_page_validations.yaml")
    def setUp(self):
        super().setUp()
        setup_info = getattr(self, "credentials", {})
        LoginPage(self).login(setup_info["url"],
                              setup_info["username"],
                              setup_info["password"])
        time.sleep(10)

    @pytest.mark.high
    @pytest.mark.regression
    @go_to_faq_section("Get Started")
    def test_get_started_categories(self):
        support_page = SupportPage(self)
        support_page.play_prezent_video()
        out = support_page.get_get_started_categories()
        if Counter(out) != Counter(list(self.suite_data.get("walkthrough_list", {}).keys())):
            self.fail(f"categories received: {out}; \n \
                      categories Expected: {self.suite_data.get("walkthrough_list", {}).keys()}")
            
        received_map = support_page.get_all_get_started_text()    
        for category, category_text in self.suite_data.get("walkthrough_list", {}).items():
            if received_map.get(category, None) is not None:
                if normalize_text(received_map[category]) == str(category_text):
                    self.fail(f"Expected Text {category_text} is not found for \
                              {category}, received: {received_map.get(category, "isempty")}")
            else:
                self.fail(f"{category} not found in {received_map}")

    @go_to_faq_section("FAQs")
    def test_faq_categories(self):
        support_page = SupportPage(self)
        out = support_page.get_faq_categories()
        if Counter(out) != Counter(self.suite_data.get("category_list", [])):
            self.fail(f"categories received: {out}; \n \
                      categories Expected: {self.suite_data.get("category_list", [])}")
        for defined_faqs in self.suite_data.get("categories", []):
            for faq_category, faq_contents in defined_faqs.items():
                support_page.navigate_to_specific_faq(faq_category_name=faq_category)
                value = support_page.get_all_faq_question_answers()
                matched_count = 0
                for line in faq_contents:
                    if normalize_text(line["question"]) in value.keys():
                        if normalize_text(line["answer"]) == value[normalize_text(line["question"])]:
                            matched_count += 1
                if matched_count == len(faq_contents):
                    print("all are matched")
                else:
                    self.fail(f"Not all question answers match for {faq_category}")
                support_page.go_back_to_faq_category()

    @pytest.mark.regression
    def test_send_support_request(self):
        support_page = SupportPage(self)
        # support button at the bottom
        support_page.navigate_to_support_page()
        support_page.navigate_to_send_support_request()
        support_page.enter_message_for_support("Testing Automation Request")
        support_page.submit_support_request()
        time.sleep(3)
        received_message = support_page.get_support_confirmation_message()
        if normalize_text(self.suite_data.get("support_confirmation_message")) == received_message:
            print("received suport confirmation message")
        else:
            failed_text = f"Expected: {self.suite_data['support_confirmation_message']}\n \
                            received: {received_message}"
            self.fail(failed_text)    
        support_page.support_submit_completion()
        time.sleep(5)

        # support buttom at the top
        support_page.navigate_to_send_support_request_at_top()
        support_page.enter_message_for_support("Testing Automation Request from top button")
        support_page.submit_support_request()
        time.sleep(3)
        received_message = support_page.get_support_confirmation_message()
        if normalize_text(self.suite_data.get("support_confirmation_message")) == received_message:
            print("received suport confirmation message")
        else:
            failed_text = f"Expected: {self.suite_data['support_confirmation_message']}\n \
                            received: {received_message}"
            self.fail(failed_text)    
        support_page.support_submit_completion()
        time.sleep(5)


    @pytest.mark.low
    def test_pro_tip(self):
        support_page = SupportPage(self)
        support_page.navigate_to_support_page()
        if support_page.is_protip_enabled() == False:
            support_page.enable_pro_tip()
            assert support_page.is_protip_enabled() is True, "Pro Tip does not show enabled "
        support_page.disable_pro_tip()
        assert support_page.is_protip_enabled() is False, "Pro Tip does not show disabled even after disabling it"

    @pytest.mark.low
    def test_search(self):
        support_page = SearchInAPage(self)
        support_page.hyrid_search("Slide")
        self.assert_page_contains("Slide Library")
        time.sleep(10)