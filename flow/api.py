from flask import Flask, render_template
from flask_restful import reqparse
from task import amazon_links, add_consumer
from apihelper import run_video, check_link

app = Flask(__name__)

@app.route("/youtube-url/", strict_slashes=False, methods=["POST"])
def youtube_post():
    parser = reqparse.RequestParser()
    parser.add_argument("video_id")
    parser.add_argument("link")
    parser.add_argument("channel_id")
    args = parser.parse_args()
    
    channel_id = args["channel_id"]
    video_id = args["video_id"]
    youtube_link = args["link"]
    
    payload = run_video(channel_id, video_id, youtube_link)

    return {"message":payload}



@app.route("/link-check/", strict_slashes=False, methods=["POST"])
def link_check():
    parser = reqparse.RequestParser()
    parser.add_argument("video_id")
    parser.add_argument("link")
    parser.add_argument("channel_id")
    args = parser.parse_args()
    
    channel_id = args["channel_id"]
    video_id = args["video_id"]
    youtube_link = args["link"]
    
    JSON = check_link(channel_id, video_id, youtube_link)
    
    return JSON


# Welcome to PEEWEE
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    



