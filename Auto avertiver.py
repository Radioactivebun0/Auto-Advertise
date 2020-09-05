from multiprocessing import Process
import sys
import time
import keyboard
import random

rocket = 0

def func1():
    global rocket
    if rocket == 0:
        print('start func1')
    while rocket < sys.maxint:
        rocket += 1
        # add code here
        Tsleep = random.randint(2100, 3600)
        Tsleep_str = str(Tsleep)
        print('avetisment delay: ' + Tsleep_str)
        time.sleep(Tsleep)
        Avt()
        time.sleep(0.1)
    print('end func1')

def Avt():
    PrintAvt = [':derp_potato: Do You Want A Fun SMP Server?:derp_potato: ', ':ender_dragon: Are You Tired Of Griefers and Hackers?:ender_dragon: ', ':steve_thumbsup: Then Vanilla Craft is the right server for you!:steve_thumbsup: ', ':mojang_old: We are a small java server with a non-toxic community:mojang_old: ', ':command_block_i: Staff are always active on discord if you need help!:command_block_i: ', 'If you would like to join us, DM me!']
    print(PrintAvt[1])
    print('Typing...')
    keyboard.write(PrintAvt[0])
    keyboard.press_and_release('shift+enter')
    keyboard.write(PrintAvt[1])
    keyboard.press_and_release('shift+enter')
    keyboard.write(PrintAvt[2])
    keyboard.press_and_release('shift+enter')
    keyboard.write(PrintAvt[3])
    keyboard.press_and_release('shift+enter')
    keyboard.write(PrintAvt[4])
    keyboard.press_and_release('shift+enter')
    keyboard.write(PrintAvt[5])
    keyboard.press_and_release('enter')
    print('Done')


def func2():
    global rocket
    if rocket == 0:
        print('start func2')
    while rocket < sys.maxint:
        rocket += 1
        # add code here
        keyboard.wait()
        give_enchated_apples()
        time.sleep(0.1)
    print('end func2')

def give_enchated_apples():
    print('giving enchanted golden apples')
    keyboard.press_and_release('t')
    time.sleep(0.15)
    keyboard.press_and_release('enter')
    time.sleep(0.15)
    keyboard.write('.give appleenchanted 64')
    time.sleep(0.15)
    keyboard.press_and_release('enter')
    time.sleep(0.15)
    keyboard.press_and_release('esc')
    func2()

def func3():
    global rocket
    if rocket == 0:
        print ('start func3')
    while rocket < sys.maxint:
        rocket += 1
        # add code here
        keyboard.wait('ctrl+l')
        stop_all()
    print ('end func3')

def stop_all():
    quit()

if __name__=='__main__':
    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()
    p3 = Process(target = func3())
    p1.join()
    p2.join()
    p3.join()