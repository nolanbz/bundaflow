from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from browser import driver
import elementfilter
import time

def get_store_links(store_link):

    browser = driver()
    response = dict()
    amazon_links = list()
    category_links = list()
    
    browser.get(store_link)
    link_path = "//a[@class='a-link-normal']"

    try:
        WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, link_path)))

        elements = browser.find_elements_by_xpath(link_path)

        for ele in elements:
            category_links.append(ele.get_attribute("href"))
            
    except TimeoutException:
        
        print("Failed to load amazon store... keeping flow")
    
    browser.save_screenshot('screenie.png')


    for link in category_links:
        browser.get(link)
       
        try:
            WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, link_path)))
        
            links = browser.find_elements_by_xpath(link_path)
            amazon_chunk = elementfilter.store_filter(links)

            for link in amazon_chunk:
                amazon_links.append(link)

        except:
            print("Failed to get category")

    browser.quit()

    response = {"amazon_links": amazon_links}

    print(response)

    return response