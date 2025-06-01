# import head is this file, do not import any project files here.

from selenium.webdriver.common.action_chains import ActionChains

def mouse_click(sb_object, locator, by="xpath"):
    element = sb_object.driver.find_element(by, locator)
    actions = ActionChains(sb_object.driver)
    actions.move_to_element(element).click().perform()