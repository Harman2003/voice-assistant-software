import os
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:3000/index.html"')

    eel.start('index.html', mode=None, host='localhost', port=3000)

if __name__ == '__main__':
    start()