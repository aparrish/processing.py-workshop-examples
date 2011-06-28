
class Sketch(object):
	def setup(self):
		size(400, 240)
		self.letters = ""
		self.display_count = 6

	def draw(self):
		background(0)
		fill(64, 240, 64)
		textAlign(CENTER, CENTER)
		textSize(72)
		# display the last n characters of string, where n is defined in the
		# "display_count" variable above (we don't need to declare it "global"
		# because we are only reading it, not modifying its value)
		text(self.letters[-self.display_count:], width/2, height/2)

	def keyPressed(self):
		if key != CODED:
			self.letters += chr(key) # chr(key) because python wants a string, not an int!

sketch = Sketch()
def setup():
	sketch.setup()
def draw():
	sketch.draw()
def keyPressed():
	sketch.keyPressed()
