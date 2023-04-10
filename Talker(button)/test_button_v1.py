from gpiozero import Button
import time

button = Button(17,None,True)

while True:
	if button.is_pressed:
	    print("1")
	else:
	    print("2")

time.sleep(0.1)
