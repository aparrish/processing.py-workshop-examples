
class Sketch(object):
	def setup(self):
		size(512, 512)
		smooth()
		self.image = loadImage("alf.jpg")

	def draw(self):
		background(0)
		#image(self.image, 0, 0)
		noStroke()
		r = 0 # radius
		theta = 0 # angle
		ellipse_size = 3
		img_center_x = self.image.width / 2
		img_center_y = self.image.height / 2
		# draw 10000 ellipses in a spiral, sampling color from the source
		# image (using its get() method)
		for i in range(10000):
			# convert polar coordinate to cartesian
			x = r * cos(theta)
			y = r * sin(theta)

			col = self.image.get(int(img_center_x + x), int(img_center_y + y))

			fill(col)
			ellipse(width/2 + x, height/2 + y, ellipse_size, ellipse_size)

			# gradually increase radius and angle according to mouse
			# position
			r += 0.1 + ((mouseX / float(width)) * 0.4)
			theta += 0.1 + ((mouseY / float(height)) * 0.2)
			ellipse_size += 0.02

sketch = Sketch()
def setup():
	sketch.setup()
def draw():
	sketch.draw()
	
