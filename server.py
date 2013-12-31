from bottle import run, route

@route('/<name>')
def index(name):
	return "Hello, " + name


if __name__ == "__main__":
	run(host="localhost", port=4000)