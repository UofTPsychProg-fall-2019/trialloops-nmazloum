#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
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
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

#stimulus

stim = ['1.jpg','2.jpg','5.jpg']
np.random.shuffle(stim)

#fixation

for x in range(len(stim)):
    fixation = visual.TextStim(win=win,pos=[0,0],text='+',color='black')
    fixation.draw()
    win.flip()
    core.wait(1)
    
    #faces loop and responses
    temp = stim[x]
    file= '/Users/seyeeh-negarmazloomfarzaghi/Desktop/faces/'+temp
    current_stim = visual.ImageStim(win, image=file, pos=(0,.2))
    text=visual.TextStim(win,text="Male or Female",pos=(0,-0.2),color='black')
    
    current_stim.draw()
    text.draw()
    
    win.flip()
    keys = event.waitKeys(keyList= ('m','f'))
    print(keys)
    
    
  
    
   
    
 




