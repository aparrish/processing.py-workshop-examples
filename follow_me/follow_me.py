def setup():
	size(400, 240)

def draw():
	background(255)
	stroke(0)
	strokeWeight(10)
	rectMode(CENTER)
	square_size = 48 + 24 * sin(frameCount * 0.1)
	if mousePressed:
		fill(240, 32, 32)
	else:
		fill(127)
	rect(mouseX, mouseY, square_size, square_size)

