#!/usr/bin/env python3

# AUTO QUICK CLICK
# 120920 zed

import pyautogui as pg
from pynput.keyboard import Key, KeyCode, Listener
import threading
import time


start_stop_key = KeyCode(char='z')
exit_key = KeyCode(char='q')
delay = 0.0001
dodebug = False

class clicker(threading.Thread):

    def __init__(self, delay):
        super(clicker, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def debugger(self, msg):
        if dodebug:
            print(msg)

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        self.debugger("Running")
        while self.program_running:
            while self.running:
                pg.click()
                time.sleep(self.delay)
            time.sleep(0.001)


click_thread = clicker(delay)
click_thread.start()

def debugger(msg):
    if dodebug:
        print(msg)

def on_press(key):
    if key == start_stop_key:
        debugger("Start stop detected")
        if click_thread.running:
            print("Stopped")
            click_thread.stop_clicking()
        else:
            print("Started")
            click_thread.start_clicking()
    elif key == exit_key:
        debugger("Exit detected")
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    header = [r" ____   ___ _____ ____ _   _  ______   __  ___ _   _  ____ ", r"| __ ) / _ \_   _/ ___| | | |/ ___\ \ / / |_ _| \ | |/ ___|", r"|  _ \| | | || || |   | |_| | |  _ \ V /   | ||  \| | |    ", r"| |_) | |_| || || |___|  _  | |_| | | |    | || |\  | |___ ", r"|____/ \___/ |_| \____|_| |_|\____| |_|   |___|_| \_|\____|"]
    for line in header:
        print(line)
    print()
    print("Z to start/stop")
    print("Q to quit")
    listener.join()


