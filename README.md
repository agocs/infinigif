Infinigif
=========

The server that responds with an endless, procedurally generated GIF image.

What it do?
-----------

Infinigif is an HTTP server that listens for requests. When it receives one, it responds with:

    HTTP/1.1 200 OK
	Content Type: image/gif
	
And then a gif image that will never end. Is it a good idea? Probably not.



How it do that?
---------------

I don't know yet, but you can put good money on me eventually using Python's Bottle or Flask framework.

How I run that?
---------------

 Clone this repo, obvs. Then, run `pip install -r requirements.txt` to install the required packages (so far, just bottle and PIL). Finally, run `python server.py`.

 Status
 ------

 So far, we're just serving up one great grey gif. More gifs = the future!

 LEMME SEE
 =========

 http://162.243.76.63:4000/

 Project is running here. It may or may not be up.