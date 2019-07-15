

import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(10, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(26, gpio.OUT)


def forward(tf):
    gpio.output(7, False)
    gpio.output(10, True)
    gpio.output(24, True)
    gpio.output(26, False)
    time.sleep(tf)


def reverse(tf):
    gpio.output(7, True)
    gpio.output(10, False)
    gpio.output(24, False)
    gpio.output(26, True)
    time.sleep(tf)


def turn_left(tf):
    gpio.output(7, True)
    gpio.output(10, True)
    gpio.output(24, True)
    gpio.output(26, False)
    time.sleep(tf)


def turn_right(tf):
    gpio.output(7, False)
    gpio.output(10, True)
    gpio.output(24, False)
    gpio.output(26, False)
    time.sleep(tf)


def pivot_left(ts):
    gpio.output(7, True)
    gpio.output(10, False)
    gpio.output(24, True)
    gpio.output(26, False)
    time.sleep(ts)


def pivot_right(tx):
    gpio.output(7, False)
    gpio.output(10, True)
    gpio.output(24, False)
    gpio.output(26, True)
    time.sleep(tx)

def sit():
    gpio.output(7, False)
    gpio.output(10, False)
    gpio.output(24, False)
    gpio.output(26, False)
