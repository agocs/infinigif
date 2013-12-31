#from bottle import run, route, response
from flask import Flask, stream_with_context, request, Response
from PIL import Image
import StringIO


app = Flask(__name__)

@app.route('/stream')
def index():
	#response.content_type = "image/gif"
	return Response(stream_with_context(generate()), mimetype='image/gif')


def generate():
	img = Image.new("RGB", (1000,2000), "#666666")
	retString = StringIO.StringIO()
	img.save(retString, "GIF")
	yield retString.getvalue()


if __name__ == "__main__":
	app.run(host="localhost", port=4000)