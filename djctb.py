import mido
import pyautogui
import threading
import time

midi_name = "MixTrack Pro FX 0"

# Print the available ports
for port in mido.get_input_names():
    print(port)

def pressLeft():
    #hold for 0.2 seconds
    pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.keyUp('left')

def pressRight():
    #hold for 0.2 seconds
    pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.keyUp('right')

def holdShift():
    pyautogui.keyDown('shift')

def releaseShift():
    pyautogui.keyUp('shift')

# open the input port
with mido.open_input(midi_name) as inport:
    print("waiting for input")
    for msg in inport:
        print(msg)
        #check if the channel is 0 and the control is 6
        if msg.type == 'control_change' and msg.channel == 0 and msg.control == 6:
            #check if the value is 127
            if msg.value >= 100 and msg.value < 127:
                print("left")
                #press the left arrow key
                # start a new thread
                t = threading.Thread(target=pressLeft)
                t.start()
            #check if the value is 0
            if msg.value <= 10 and msg.value > 1:
                print("right")
                #press the right arrow key
                # start a new thread
                t = threading.Thread(target=pressRight)
                t.start()

        #check if the channel is 1 and the note is 32
        if msg.type == 'note_on' and msg.channel == 1 and msg.note == 32:
            # start a new thread
            t = threading.Thread(target=holdShift)
            t.start()

        #check if the channel is 1 and the note is 32
        if msg.type == 'note_off' and msg.channel == 1 and msg.note == 32:
            # start a new thread
            t = threading.Thread(target=releaseShift)
            t.start()



