import urllib
import simplejson
import textwrap

class Sketch(object):
	def setup(self):
		size(640, 400)

		# load tweets from twitter search
		self.tweets = list()
		resp = urllib.urlopen("http://search.twitter.com/search.json?q=kitten&rpp=100")
		search_result = simplejson.loads(resp.read())
		for tweet in search_result['results']:
			self.tweets.append(tweet['text'])

		# load images from data directory, make a list of them
		self.images = list()
		for i in range(16):
			fname = str(i) + ".jpg"
			self.images.append(loadImage(fname))

		# index of picture to show in draw()
		self.current_pic = 0

		# index of tweet to show in draw()
		self.current_tweet = 0

		# when was the last time we changed the picture, and how long
		# should we wait between pictures?
		self.last_change = millis()
		self.pic_wait = 4500

	def draw(self):
		# switch pics and tweets after self.pic_wait milliseconds
		if millis() > self.last_change + self.pic_wait:
			self.current_pic += 1
			self.current_tweet += 1
			self.last_change = millis()

		# set index to zero if we've overstepped the boundary of the
		# array
		if self.current_pic > len(self.images) - 1:
			self.current_pic = 0
		if self.current_tweet > len(self.tweets) - 1:
			self.current_tweet = 0

		image(self.images[self.current_pic], 0, 0)

		fill(255)
		textAlign(CENTER, CENTER)
		textSize(48)

		# use python textwrap library to insert linebreaks into the
		# tweet text
		text(textwrap.fill(self.tweets[self.current_tweet], 25),
				width/2, height/2)

sketch = Sketch()
def setup():
	sketch.setup()
def draw():
	sketch.draw()
	
