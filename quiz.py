from gpiozero import LED, Button
from signal import pause
from time import sleep
from pythonosc.udp_client import SimpleUDPClient as OSC
import os

reset_led = LED(18)
reset_button = Button(17, hold_time=2)

ip = "192.168.1.255"
port = 53000

client = OSC(ip, port)

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
leds = [led1, led2, led3, led4, led5, led6, led7, led8]
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


def buzz_in(player_num):
    leds[player_num-1].on()
    client.send_message("/cue/{}/start".format(player_num), 0)
    os.system('aplay /home/pi/Horn.wav')
    sleep(1)
    leds[player_num-1].off()


button1.when_pressed = (lambda: buzz_in(1))
button2.when_pressed = (lambda: buzz_in(2))
button3.when_pressed = (lambda: buzz_in(3))
button4.when_pressed = (lambda: buzz_in(4))
button5.when_pressed = (lambda: buzz_in(5))
button6.when_pressed = (lambda: buzz_in(6))
button7.when_pressed = (lambda: buzz_in(7))
button8.when_pressed = (lambda: buzz_in(8))

pause()
