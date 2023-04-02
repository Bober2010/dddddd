x = 0

def setup():
    size(600,600)
    colorMode(HSB,255)
    background(255)
def draw():
    global x

    fill(x,255,255)
    rect(mouseY, 0,mouseX ,600)
    if x == 255:
        x = 0
        0
    x += 1
