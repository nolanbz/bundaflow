from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from browser import driver
import elementfilter
from clicklink import rinse

def get_description_links(youtube_link):

    browser = driver()
    response = dict()
    clean_links = list()
    sus_elements = dict()
    
    browser.get(youtube_link)
    video_path = "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']"

    try:
        WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, video_path)))

        button_class_name = "more-button"
        link_path = "//a[@class='yt-simple-endpoint style-scope yt-formatted-string']"

        try:

            # Find show more button
            show_more_button = browser.find_element_by_class_name(button_class_name)
            # Click show more button
            show_more_button.click()
            # Get all elements in the description
            elements = browser.find_elements_by_xpath(link_path)
            # Get all clean easy to convert links
            clean_links = elementfilter.clean(elements)
            # Get all sus hard to convert link elements
            sus_elements = elementfilter.sus(elements)
            # Click on all sus links and get their true link
            sus_links = rinse(browser, sus_elements)

        except:
            print("No show more button... keeping flow")
            
    except TimeoutException:
        browser.save_screenshot("youtube.png")
        print("Failed to load youtube video link... keeping flow")

    browser.quit()

    response = {"sus_links": sus_links, "clean_links": clean_links}

    return response

def link_present(youtube_link, keyword):
    
    links = get_description_links(youtube_link)

    all_links = links["sus_links"] + links["clean_links"]

    present = elementfilter.present_link(all_links, keyword)

    return present


