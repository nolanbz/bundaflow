import requests
import json

def abunda_convert(link, check_price):

    abunda_id = int()
    payload = "https://abunda-engine.herokuapp.com/amazon-link-handler?amz_link={}&speed=true".format(link)
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    get_request = requests.get(payload, headers=headers)

    if get_request.status_code == 200:
        response = get_request.json()
        try:
            price = response["price_good"]
            # Check if price is over $50  
            if check_price:
                if price:
                    abunda_id = response["id"]
            else:
                abunda_id = response["id"]
            
        except:
            print("no abunda url returned")
    else:
        print("Failed to upload link to abunda... keeping flow")
    
    return abunda_id


def create_ids(product_links, check_price):

    abunda_ids = list()

    for link in product_links:
        converted_link = abunda_convert(link, check_price)
        if converted_link:
            abunda_ids.append(converted_link)
    
    return abunda_ids

