from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from browser import driver

def get_store_links(store_link):

    browser = driver()
    response = dict()
    amazon_links = str()
    
    
    
    browser.get(store_link)
    video_path = "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']"

    try:
        WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, video_path)))

        
            
    except TimeoutException:
        
        print("Failed to load youtube video link... keeping flow")

    browser.quit()

    response = {"amazon_links": amazon_links}

    return response