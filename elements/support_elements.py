Element_support = "#support"
Element_expand_section = "//*[contains(@class, 'help-item-title') and contains(text(), '%s')]/parent::div/div/button"

# faq
Element_faq_table = "div.faqs-content > div > div"
# xpath= "//div[@class='faqs-content']/div/div[%d]/div[@class='category-item']/span[@class='category-item__label']"
Element_faq_table_rows = "div.faqs-content > div > div:nth-of-type(%d) > div.category-item > span.category-item__label"
Element_specific_faq = "//div[@class='category-item']/span[@class='category-item__label' and contains(text(), '%s')]"
Element_expand_faq = "#faq-expand-btn"
# xpath = "//div[@class='faq-category']/following-sibling::div/div"
Element_faq_category_table = "div.v-item-group.theme--light.v-expansion-panels > div.v-expansion-panel.faq-item"
# xpath = "//div[@class='faq-category']/following-sibling::div/div[%d]/button/div[@class='faq-question']"
Element_faq_question = "div.v-item-group.theme--light.v-expansion-panels > div.v-expansion-panel.faq-item:nth-of-type(%d) > button > div.faq-question"
# xpath = "//div[@class='faq-category']/following-sibling::div/div[%d]/div/div[@class='marked-container']/p"
Element_faq_anwser = "div.v-item-group.theme--light.v-expansion-panels > div.v-expansion-panel.faq-item.v-expansion-panel--active.v-expansion-panel--next-active.v-item--active:nth-of-type(%d) > div.faq-answer > div.marked-container > p"
Element_faq_answer_last_row = "div.v-item-group.theme--light.v-expansion-panels > div.v-expansion-panel.faq-item.v-expansion-panel--active.v-item--active:nth-of-type(%d) > div.v-expansion-panel-content.faq-answer > div.marked-container > p"
# xpath= "//div[@class='faq-wrapper']/div[@class='actions-section']/span[@class='action-btn']"
Element_faq_category_back_button = "div.faq-wrapper > div.actions-section > span.action-btn"

# support request
# xapth="//div[@class='send-support-bottom']/div[@class='help-menu-actions']/button"
Element_send_support_request_button = "div.send-support-bottom > div.help-menu-actions > button"
# xpath="//div[@class='help-menu-title']/div[contains(text(), 'Help Center')]/following-sibling::button/span/span[contains(text(), 'Send support request')]"
Element_send_support_request_at_top = "button.send-support-top.v-btn.v-btn--rounded.v-btn--text.theme--light.v-size--default > span.v-btn__content > span"
# xpath="//div/label[contains(text(), 'Enter your note here...')]/following-sibling::*"
Element_support_request_text = "div.v-input__control > div.v-input__slot > div.v-text-field__slot > [id^='input-']" 
# xpath="//span[contains(text(), 'Submit')]"
Element_submit_support_request = "div.supportbox-inner > button.primary-button.v-btn--is-elevated.v-btn--has-bg.v-btn--rounded.theme--light.v-size--default"
Element_support_confirm_message = "div.support-confirm-message"
Element_support_confirm_button = "//span[contains(text(), 'Done')]" #leave it as xpath for exact button match.

# get started 
Element_get_started_expand = "//*[contains(@class, 'help-item-title') and contains(text(), 'Get Started')]/parent::div/div/button"
# xpath = "//div[@class='walkthrough-items-wrapper']/div/div"
Element_get_started_table = "div.walkthrough-items-wrapper > div.row > div"
# xpath = "//div[@class='walkthrough-items-wrapper']/div/div[%d]/div[@class='walkthrough-item']/div[@class='item-info']/div[@class='item-info-title']"
Element_get_started_table_rows = "div.walkthrough-items-wrapper > div.row > div:nth-of-type(%d) > div.walkthrough-item > div.item-info > div.item-info-title"
Element_get_started_row_help_text = "div.walkthrough-items-wrapper > div.row > div:nth-of-type(%d) > div.walkthrough-item > div.item-info > div.item-info-desc"
Element_present_overview_video = "//div[@class='overview-video']/parent::div/button"
Element_present_video_layout = "//*[@id='modals-container']/div[@class='vm--container']/div[@data-modal='TutorialVideoDetail']"

# pro tip
Element_protip_checkbox = "#protip-toggle--auto"