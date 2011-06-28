# requires opencv for processing/java, find it here:
# http://ubaa.net/shared/processing/opencv/

import hypermedia.video.OpenCV as OpenCV

class Sketch(object):
	def setup(self):
		size(640, 480)
		self.opencv = OpenCV(this)
		self.opencv.capture(width, height)
		self.opencv.cascade(OpenCV.CASCADE_FRONTALFACE_ALT)

		self.trollface = loadImage("trollface.png")

	def stop(self):
		self.opencv.stop()

	def draw(self):

		imageMode(CORNER)
		self.opencv.read()
		image(self.opencv.image(), 0, 0)

		faces = self.opencv.detect(1.2, 2, OpenCV.HAAR_DO_CANNY_PRUNING, 40, 40)

		noStroke()
		fill(255, 16)
		imageMode(CENTER)
		for face in faces:
			posx = face.x + face.width / 2
			posy = face.y + face.height / 2
			image(self.trollface, posx, posy, face.width*2, face.height*2)

sketch = Sketch()
def setup():
	sketch.setup()
def draw():
	sketch.draw()
def stop():
	sketch.stop()

