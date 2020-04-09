from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import buddon
import time

def rinse(browser, elements):
    
    print("Checking {} link(s)".format(len(elements)))

    full_links = list()
    black_list = ["youtube", "pinterest", "blogspot", "instagram", "twitter", "facebook", "goo.gl", "kit.co",
                  "discord", "banggood", "tubebuddy", "gearbest", "spinning" "mikesunboxing", "knockies", "darkhorse"]

    # Save Video tab
    original_handle = browser.current_window_handle
    
    # Loop throught sus elements
    for elm in elements:
        browser.switch_to.window(original_handle)
        check = any(x in elm.text for x in black_list)

        # Check if sus link in black list
        if not check:
            
            # Open sus link in new tab
            buddon.click(browser, elm)
            # Switch to newly opened tab
            handle = browser.window_handles[-1]
            browser.switch_to.window(handle)

            # Attempt to get current URL untill page fully loads
            i = 0
            while browser.current_url in "about:blank":
                i += 1
                time.sleep(0.5)
                if i == 20:
                    break

            # Save URL         
            full_links.append(browser.current_url)

            # Close opened tab
            for handle in browser.window_handles:
                if handle != original_handle:
                    browser.switch_to.window(handle)
                    browser.close()

    return full_links