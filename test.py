import RPi.GPIO as GPIO
import time

# if GPIO.input(button) == GPIO.HIGH:
#     test = 1

#assigning the input pins to the corresponding led (in order they appear right-left in real life)
green_one = 14
red = 18
yellow = 15
green_two = 23
blue = 25

leds = [green_one, red, yellow, green_two, blue] # creates an array of the leds for iteration purposes
ledNum = len(leds)

winning_led = 2 # the index of the array that has been selected to be the winning led
game_speed = 0.23 #time, in seconds, a led stays lit

button = 10 #input pin for the button

GPIO.setmode(GPIO.BCM) #my board has the actual pins named, so I will be using BCM instead of BOARD
#Setups the leds as output and the button as input (pull_up_down=GPIO.PUD_DOWN simply means that it is initially in the off position)
GPIO.setup(green_one, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green_two, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    while True:
        if GPIO.input(button) == GPIO.HIGH:
            time.sleep(1)
            playGame(True)
            break

def playGame(playing):
    while playing:
        if playing == False:
            break
        for i in range(0, ledNum):
            GPIO.output(leds[i], True)
            start = time.clock()
            while (time.clock() - start < game_speed):
                if (i == winning_led and GPIO.input(button) == GPIO.HIGH):
                    GPIO.output(leds[i], False)
                    flashLeds()
                    playing = False
                    return "Won"
                elif (GPIO.input(button) == GPIO.HIGH):
                    GPIO.output(leds[i], False)
                    flashLosingRed()
                    playing = False
                    return "Lost"
            GPIO.output(leds[i], False)

def flashLeds():
    for x in range(0, 4):
        for i in range(0, ledNum):
            GPIO.output(leds[i], True)
        time.sleep(0.5)
        for i in range(0, ledNum):
            GPIO.output(leds[i], False)
        time.sleep(0.5)

def flashLosingRed():
    for i in range(0, 10):
        GPIO.output(red, True)
        time.sleep(0.2)
        GPIO.output(red, False)
        time.sleep(0.2)


if __name__ == "__main__":
    main()