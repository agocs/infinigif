from bottle import run, route, response
from PIL import Image
import StringIO

@route('/')
def index():
	response.content_type = "image/gif"
	img = Image.new("RGB", (1000,2000), "#666666")
	retString = StringIO.StringIO()
	img.save(retString, "GIF")

	return retString.getvalue()



if __name__ == "__main__":
	run(host="localhost", port=4000)