from flask import Flask, stream_with_context, request, Response
from PIL import Image
import StringIO
import hashlib

app = Flask(__name__)

@app.route('/')
def index():


	return Response(stream_with_context(generate(request.remote_addr)), mimetype='image/gif')


def generate(ip_addr):

	color = hashlib.md5(ip_addr).hexdigest()[0:6]
	img = Image.new("RGB", (1000,2000), "#"+color)
	retString = StringIO.StringIO()
	img.save(retString, "GIF")
	yield retString.getvalue()


if __name__ == "__main__":
	app.run(host="localhost", port=4000)