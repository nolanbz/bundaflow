from flask import Flask, render_template
from flask_restful import reqparse
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from task import amazon_links, add_consumer
from apihelper import run_video, check_link, store_upload
import os

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {username: generate_password_hash(password)}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route("/youtube-url/", strict_slashes=False, methods=["POST"])
@auth.login_required
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
@auth.login_required
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

@app.route("/store-upload/", strict_slashes=False, methods=["POST"])
@auth.login_required
def upload_store():
    parser = reqparse.RequestParser()
    parser.add_argument("store_url")
    parser.add_argument("channel_id")
    args = parser.parse_args()
    
    channel_id = args["channel_id"]
    store_url = args["store_url"]
    
    payload = store_upload(channel_id, store_url)
    
    return {"message":payload}


# Welcome to PEEWEE
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    




