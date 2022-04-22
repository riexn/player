from focusVLC import closeVLC
import time
import os
import subprocess

def startPlaylist(folderPath):
    closeVLC()
    time.sleep(0.25)
    os.system(f'start vlc "{folderPath}"')
