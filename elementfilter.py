import requests
# Get all http links from description
def http(description_elements):
    elements = list()

    for ele in description_elements:
        if "http" in ele.text:
            elements.append(ele)

    return elements

# Get all non truncated links from description
def clean(description_elements):

    short_links = list()
    full_links = list()

    clean_elements = http(description_elements)
    for ele in clean_elements:
        if "..." not in ele.text:
            short_links.append(ele.text)

    for link in short_links:
        try:
            data = requests.request("GET", link)
            url = data.url
            full_links.append(url)
        except:
            print("Failed to get full link... keeping flow")

    return full_links

# Get all truncated links from description
def sus(description_elements):
    elements = list()
    clean_elements = http(description_elements)

    for ele in clean_elements:
        if "..." in ele.text:
            elements.append(ele)

    return elements

def product(links):
    product_links = list()

    for link in links:
        if "amazon.com" in link:
            if "shop" not in link:
                product_links.append(link)
    
    return product_links

def shop(links):
    shop_links = list()

    for link in links:
        if "amazon.com" in link:
            if "shop" in link:
                shop_links.append(link)

    return shop_links

def present_link(links, keyword):
    present = bool()
    
    for link in links:
        if keyword in link:
            present = True
    
    return present

def all_links(description_elements):
    elements = list()

    for ele in description_elements:
        if "http" in ele.text:
            elements.append(ele.text)

    return elements


def store_filter(description_elements):
    links = list()

    for ele in description_elements:
        link = ele.get_attribute("href")
        if "shop" not in link:
            links.append(link)

    return links
