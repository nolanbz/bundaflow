from celery import Celery
from abunda import create_ids
from description import get_description_links
import elementfilter
import os
import posts

app = Celery()
app.conf.broker_url = os.environ.get("CLOUDAMQP_URL")

def add_consumer(channel_id):    
    app.control.add_consumer(queue=channel_id, auto_delete=True, reply=True)

@app.task
def amazon_links(channel_id, video_id, youtube_link):
    
    video_views = str()
    # TODO get view views with bs
    
    links = get_description_links(youtube_link)
    all_links = links["sus_links"] + links["clean_links"]
    product_links = elementfilter.product(all_links)
    shop_links = elementfilter.shop(all_links)
    abunda_ids = create_ids(product_links)

    posts.big_post(channel_id, video_id, video_views, abunda_ids, shop_links)
    
    