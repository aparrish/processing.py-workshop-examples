
class Sketch(object):
	def setup(self):
		size(512, 512)
		smooth()
		self.image = loadImage("alf.jpg")

	def draw(self):
		background(0)
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

			col = self.image.get(int(mouseX + x), int(mouseY + y))

			fill(col)
			ellipse(mouseX + x, mouseY + y, ellipse_size, ellipse_size)

			# gradually increase radius and angle
			r += 0.2
			theta += 0.5
			ellipse_size += 0.01

sketch = Sketch()
def setup():
	sketch.setup()
def draw():
	sketch.draw()
