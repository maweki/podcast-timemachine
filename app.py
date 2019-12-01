from flask import Flask, send_file, request, abort, Response
from ptm import delayFeed

app = Flask(__name__)

@app.route("/")
def root():
    return send_file("page.html")

@app.route("/rss/", methods=['GET'])
def rss():
    try:
        feed = request.args.get('feed')
        delay = int(request.args.get('delay'))
        xml = delayFeed(feed, delay)
        return Response(xml, mimetype='text/xml')
    except:
        abort(500)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
