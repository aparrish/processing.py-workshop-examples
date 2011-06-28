
display_count = 6
letters = ""

def setup():
	size(400, 240)

def draw():
	background(0)
	fill(64, 240, 64)
	textAlign(CENTER, CENTER)
	textSize(72)
	# display the last n characters of string, where n is defined in the
	# "display_count" variable above (we don't need to declare it "global"
	# because we are only reading it, not modifying its value)
	text(letters[-display_count:], width/2, height/2)

def keyPressed():
	global letters # declared global so we can modify it
	if key != CODED:
		letters += chr(key) # chr(key) because python wants a string, not an int!
	print key

