
from task import amazon_links, add_consumer
from description import link_present

def run_video(channel_id, video_id, youtube_link):

    payload = str()

    if channel_id:
        if video_id:
            if youtube_link:
                payload = "converting"
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
                payload = "we workin"
            else:
                payload = "missing link", 400
        else:
            payload = "missing video_id", 400
    else:
        payload = "missing channel_id", 400

    JSON = {"video_id": video_id, "channel_id": channel_id, "links_present": detected, "message":payload}


    return JSON