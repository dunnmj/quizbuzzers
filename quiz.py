from gpiozero import LED, Button
from signal import pause
from time import sleep

reset_led = LED(18)
reset_button = Button(17, hold_time=2)

button1 = Button(21, pull_up=False)
button2 = Button(20, pull_up=False)
button3 = Button(16, pull_up=False)
button4 = Button(12, pull_up=False)
button5 = Button(7, pull_up=False)
button6 = Button(8, pull_up=False)
button7 = Button(25, pull_up=False)
button8 = Button(24, pull_up=False)

led1 = LED(26)
led2 = LED(19)
led3 = LED(13)
led4 = LED(6)
led5 = LED(5)
led6 = LED(11)
led7 = LED(9)
led8 = LED(10)

toggle = 1


def reset_press():
    global toggle
    toggle = 0
    reset_led.off()
    print("Resetting...")


reset_button.when_held = reset_press
reset_led.on()

while toggle == 1:
    led8.off()
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    led3.on()
    sleep(1)
    led3.off()
    led4.on()
    sleep(1)
    led4.off()
    led5.on()
    sleep(1)
    led5.off()
    led6.on()
    sleep(1)
    led6.off()
    led7.on()
    sleep(1)
    led7.off()
    led8.on()
    sleep(1)

print("Play Begins...")

while True:
    while toggle == 0:
        if GPIO.input(switch1) == 0:
            GPIO.output(relay1, 1)
            toggle = 1
            print("Player 1 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player1.mp3')
            break
        if GPIO.input(switch2) == 0:
            GPIO.output(relay2, 1)
            toggle = 1
            print("Player 2 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player2.mp3')
            break
        if GPIO.input(switch3) == 0:
            GPIO.output(relay3, 1)
            toggle = 1
            print("Player 3 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player3.mp3')
            break
        if GPIO.input(switch4) == 0:
            GPIO.output(relay4, 1)
            toggle = 1
            print("Player 4 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player4.mp3')
            break
        if GPIO.input(switch5) == 0:
            GPIO.output(relay5, 1)
            toggle = 1
            print("Player 5 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player5.mp3')
            break
        if GPIO.input(switch6) == 0:
            GPIO.output(relay6, 1)
            toggle = 1
            print("Player 6 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player6.mp3')
            break
        if GPIO.input(switch7) == 0:
            GPIO.output(relay7, 1)
            toggle = 1
            print("Player 7 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player7.mp3')
            break
        if GPIO.input(switch8) == 0:
            GPIO.output(relay8, 1)
            toggle = 1
            print("Player 8 Buzzed")
            print("Press Reset...")
            os.system('mplayer -really-quiet /media/usb0/player8.mp3')
            break

    GPIO.output(reset_led, 1)

    while toggle == 1:
        print("Waiting for reset")
        GPIO.wait_for_edge(reset_switch, GPIO.RISING)
        reset_press(reset_switch)

    GPIO.output(relay1, 0)
    GPIO.output(relay2, 0)
    GPIO.output(relay3, 0)
    GPIO.output(relay4, 0)
    GPIO.output(relay5, 0)
    GPIO.output(relay6, 0)
    GPIO.output(relay7, 0)
    GPIO.output(relay8, 0)
    print("System Reset")
