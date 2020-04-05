from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sys import platform

def click(browser, link):
    
    if platform == "darwin":
        ActionChains(browser) \
            .key_down(Keys.COMMAND) \
            .click(link) \
            .key_up(Keys.COMMAND) \
            .perform()
    else:
        ActionChains(browser) \
            .key_down(Keys.CONTROL) \
            .click(link) \
            .key_up(Keys.CONTROL) \
            .perform()