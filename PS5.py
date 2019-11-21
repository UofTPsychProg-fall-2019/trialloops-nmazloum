#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window
# so that you can still see your console
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging
event.globalKeys.add(key='q',func=core.quit)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white')

Female1=visual.ImageStim(win,'/Users/seyeeh-negarmazloomfarzaghi/Desktop/faces/''5.jpg')

text=visual.TextStim(win,text="Male or Female",pos=(0,-0.2),color='black')

# then draw all stimuli
Female1.draw()

text.draw()
# then flip your window

win.flip()
# then record your responses

keys=event.waitKeys(keyList=('m','f'))

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

print(keys)
core.wait(2)
win.close()