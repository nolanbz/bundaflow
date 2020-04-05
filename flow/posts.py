import requests
import os

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

def big_post(channel_id, video_id, video_views, abunda_ids, shop_links):
    
    JSON = {"channel_id": channel_id, "video_id": video_id, "views": video_views, "abunda_ids": abunda_ids, "shop_links": shop_links}

    post_url = "https://{}:{}@abunda-engine.herokuapp.com/video_callbacks/receive_data".format(username, password)
       
    requests.post(post_url, json=JSON)