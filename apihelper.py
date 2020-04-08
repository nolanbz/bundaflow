
from task import amazon_links, add_consumer, amazon_store
from description import link_present

def run_video(channel_id, video_id, youtube_link):

    payload = str()

    if channel_id:
        if video_id:
            if youtube_link:
                payload = "Converting"
                amazon_links.apply_async((channel_id, video_id, youtube_link), queue=channel_id)
                add_consumer(channel_id)
            else:
                payload = "missing link", 400
        else:
            payload = "missing video_id", 400
    else:
        payload = "missing channel_id", 400
    
    return payload



def check_link(channel_id, video_id, youtube_link):

    detected = False

    if channel_id:
        if video_id:
            if youtube_link:
                detected = link_present(youtube_link, "abunda")
                payload = "Checking link"
            else:
                payload = "missing link", 400
        else:
            payload = "missing video_id", 400
    else:
        payload = "missing channel_id", 400

    JSON = {"video_id": video_id, "channel_id": channel_id, "links_present": detected, "message":payload}


    return JSON

def store_upload(channel_id, store_link):

    payload = str()

    if channel_id:        
        if store_link:
            payload = "Uploading store"
            amazon_store.apply_async((channel_id, store_link), queue=channel_id)
            add_consumer(channel_id)
        else:
            payload = "missing store link", 400
    else:
        payload = "missing channel_id", 400
    
    return payload