from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from browser import driver

import time

def get_store_links(store_link):

    browser = driver()
    response = dict()
    amazon_links = str()
    
    
    
    browser.get(store_link)
    link_path = "//a[@class='a-link-normal']/div[@class='overlay']"

    try:
        WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, link_path)))

        elements = browser.find_elements_by_xpath(link_path)


        for ele in elements:
            
            ele.click()
            time.sleep(3)
            links = browser.find_elements_by_xpath("//a[@class='a-link-normal']")
            
            print(len(links))
            for link in links:
                
                href = link.find_element_by_class_name("a-link-normal").get_attribute("href")
                # href = link.find_element_by_class_name("a-link-normal")
                print(href)


        
            
    except TimeoutException:
        
        print("Failed to load amazon store... keeping flow")

    browser.quit()

    response = {"amazon_links": amazon_links}

    return response

store = "https://www.amazon.com/shop/tronicsfix"
get_store_links(store)