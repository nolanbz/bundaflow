from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from browser import driver
import elementfilter
from clicklink import rinse

def get_views(browser):

    video_views = str()
    view_path = "//span[@class='view-count style-scope yt-view-count-renderer']"

    try:
        view_count = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, view_path)))
        video_views = view_count.text.replace(" views", "")
    except:
        print("Unable to find view count... keeping flow")

    return video_views

def get_description_links(youtube_link, rinse_links):

    browser = driver()
    response = dict()
    clean_links = list()
    sus_links = list()
    sus_elements = dict()
    video_views = str()
    all_links = list()
    
    browser.get(youtube_link)
    video_path = "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']"

    try:
        WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, video_path)))

        button_class_name = "more-button"
        link_path = "//a[@class='yt-simple-endpoint style-scope yt-formatted-string']"

        try:

            # Get Video views
            video_views = get_views(browser)
            # Find show more button
            show_more_button = browser.find_element_by_class_name(button_class_name)
            # Click show more button
            show_more_button.click()
            # Get all elements in the description
            elements = browser.find_elements_by_xpath(link_path)

            # Used for checking if links are present in description
            if rinse_links:
                all_links = elementfilter.all_links(elements)
                response = {"all_links": all_links}
                browser.quit()
                return response


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

    response = {"sus_links": sus_links, "clean_links": clean_links, "video_views": video_views, "all_links": all_links }

    return response

def link_present(youtube_link, keyword):
    
    links = get_description_links(youtube_link, True)

    all_links = links["all_links"]

    present = elementfilter.present_link(all_links, keyword)

    return present
