from pytube import YouTube
from flask import Flask, render_template, url_for, request
import time
from hurry.filesize import size

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/youtube")
def youtube():
    url = request.args.get("url")
    if url:
        yt = YouTube(url)
        video = {
            "info": {
                "title": yt.title,
                "author": yt.author,
                "thumbnail": yt.thumbnail_url,
                "desc": yt.description,
                "time": time.strftime("%H:%M:%S", time.gmtime(yt.length)),
                "views": yt.views,
                "publish_date": yt.publish_date
            },
            "sources": []
        }
        videos = yt.streams.filter(progressive=True)
        for v in videos:
            video["sources"].append({
                "url": v.url,
                "quality": v.resolution,
                "size": size(v.filesize)
            })
        return video
