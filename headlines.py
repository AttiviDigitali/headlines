from flask import Flask
from flask import render_template

import feedparser

ansa = 'http://www.ansa.it/sito/notizie/cultura/cultura_rss.xml'

app = Flask(__name__)


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(ansa)
    return render_template("home.html", articles = feed.entries)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
