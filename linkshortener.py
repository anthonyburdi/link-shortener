from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from random import randint
import urllib2

app = Flask(__name__)
my_ip = urllib2.urlopen('http://checkip.amazonaws.com').read().rstrip()

links = {} # Global list of links, in memory. Could be persisted.

@app.route('/', methods=['POST', 'GET'])
def shorten():
	"""Create a shortlink from input link"""
	error = None
	if request.method == 'POST':
		link = request.form['link'] # receive the entered link
		shortlink = shortLink(links) # create shortlink
		links[shortlink] = link # place shortlink into global dict
		return render_template('shortener.html', link=link, 
			shortlink=shortlink, error=error, links=links, my_ip=my_ip)
	if request.method == 'GET':
		return render_template('shortener.html')

@app.route('/<shortlink>')
def reroute(shortlink):
	"""Redirect from shortlink to original url"""
	return redirect(links[int(shortlink)], code=302)

def shortLink(links):
	"""Return a shortlink code, randomly generated but checked for
	uniqueness"""
	# Generate random code
	code = randint(10000,99999)
	# If random code was already used, generate a new one until it's
	# unique
	while code in links:
		code = randint(10000,99999)
	return code

if __name__ == '__main__':
	# app.debug = True
	app.run(port=5001, host='0.0.0.0') # Port 5000 giving errors, shared w Apple
