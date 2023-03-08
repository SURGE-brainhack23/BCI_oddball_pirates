#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Mar  8 00:30:41 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'oddball_pirates'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/brynn/Desktop/BCI_oddball_pirates/oddball_pirates_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='hex',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Welcome_Message" ---
Welcome2 = visual.TextStim(win=win, name='Welcome2',
    text='Welcome to the experiment!\nPress the space bar to start.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keywelcome2 = keyboard.Keyboard()

# --- Initialize components for Routine "Fixation_cross" ---
fixationcross_3 = visual.ImageStim(
    win=win,
    name='fixationcross_3', 
    image='images/fixation_cross_pink.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil1_4 = visual.ImageStim(
    win=win,
    name='sil1_4', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil2_4 = visual.ImageStim(
    win=win,
    name='sil2_4', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil3_4 = visual.ImageStim(
    win=win,
    name='sil3_4', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil4_4 = visual.ImageStim(
    win=win,
    name='sil4_4', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil5_4 = visual.ImageStim(
    win=win,
    name='sil5_4', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
sil6_4 = visual.ImageStim(
    win=win,
    name='sil6_4', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Target_Highlight" ---
sil1_5 = visual.ImageStim(
    win=win,
    name='sil1_5', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil2_5 = visual.ImageStim(
    win=win,
    name='sil2_5', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil3_5 = visual.ImageStim(
    win=win,
    name='sil3_5', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil4_5 = visual.ImageStim(
    win=win,
    name='sil4_5', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil5_5 = visual.ImageStim(
    win=win,
    name='sil5_5', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil6_5 = visual.ImageStim(
    win=win,
    name='sil6_5', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
highlight_ = visual.ImageStim(
    win=win,
    name='highlight_', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Trial" ---
sil1_6 = visual.ImageStim(
    win=win,
    name='sil1_6', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil2_6 = visual.ImageStim(
    win=win,
    name='sil2_6', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil3_6 = visual.ImageStim(
    win=win,
    name='sil3_6', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil4_6 = visual.ImageStim(
    win=win,
    name='sil4_6', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil5_6 = visual.ImageStim(
    win=win,
    name='sil5_6', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil6_6 = visual.ImageStim(
    win=win,
    name='sil6_6', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
stim_2 = visual.ImageStim(
    win=win,
    name='stim_2', 
    image='sin', mask=None, anchor='center',
    ori=1.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Break" ---
text = visual.TextStim(win=win, name='text',
    text='Take at least a minute to rest.  \n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Required break finished.\n\nOnce you feel refreshed, press the spacebar to continue with the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Example_end" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='End of silhouettes\n\nPress the spacebar to continue onto the faces',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "Fixation_cross" ---
fixationcross_3 = visual.ImageStim(
    win=win,
    name='fixationcross_3', 
    image='images/fixation_cross_pink.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil1_4 = visual.ImageStim(
    win=win,
    name='sil1_4', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil2_4 = visual.ImageStim(
    win=win,
    name='sil2_4', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil3_4 = visual.ImageStim(
    win=win,
    name='sil3_4', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil4_4 = visual.ImageStim(
    win=win,
    name='sil4_4', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil5_4 = visual.ImageStim(
    win=win,
    name='sil5_4', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
sil6_4 = visual.ImageStim(
    win=win,
    name='sil6_4', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Target_Highlight" ---
sil1_5 = visual.ImageStim(
    win=win,
    name='sil1_5', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil2_5 = visual.ImageStim(
    win=win,
    name='sil2_5', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil3_5 = visual.ImageStim(
    win=win,
    name='sil3_5', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil4_5 = visual.ImageStim(
    win=win,
    name='sil4_5', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil5_5 = visual.ImageStim(
    win=win,
    name='sil5_5', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil6_5 = visual.ImageStim(
    win=win,
    name='sil6_5', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
highlight_ = visual.ImageStim(
    win=win,
    name='highlight_', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Trial" ---
sil1_6 = visual.ImageStim(
    win=win,
    name='sil1_6', 
    image='images/stim_silhouettes/pirate1_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sil2_6 = visual.ImageStim(
    win=win,
    name='sil2_6', 
    image='images/stim_silhouettes/pirate2_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
sil3_6 = visual.ImageStim(
    win=win,
    name='sil3_6', 
    image='images/stim_silhouettes/pirate3_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sil4_6 = visual.ImageStim(
    win=win,
    name='sil4_6', 
    image='images/stim_silhouettes/pirate4_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
sil5_6 = visual.ImageStim(
    win=win,
    name='sil5_6', 
    image='images/stim_silhouettes/pirate5_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
sil6_6 = visual.ImageStim(
    win=win,
    name='sil6_6', 
    image='images/stim_silhouettes/pirate6_sil.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
stim_2 = visual.ImageStim(
    win=win,
    name='stim_2', 
    image='sin', mask=None, anchor='center',
    ori=1.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Break" ---
text = visual.TextStim(win=win, name='text',
    text='Take at least a minute to rest.  \n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Required break finished.\n\nOnce you feel refreshed, press the spacebar to continue with the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Finish" ---
text_9 = visual.TextStim(win=win, name='text_9',
    text='That concludes the experiment!\n\nThank you for participating. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome_Message" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keywelcome2.keys = []
keywelcome2.rt = []
_keywelcome2_allKeys = []
# keep track of which components have finished
Welcome_MessageComponents = [Welcome2, keywelcome2]
for thisComponent in Welcome_MessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome_Message" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome2* updates
    if Welcome2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Welcome2.frameNStart = frameN  # exact frame index
        Welcome2.tStart = t  # local t and not account for scr refresh
        Welcome2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome2.started')
        Welcome2.setAutoDraw(True)
    
    # *keywelcome2* updates
    waitOnFlip = False
    if keywelcome2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        keywelcome2.frameNStart = frameN  # exact frame index
        keywelcome2.tStart = t  # local t and not account for scr refresh
        keywelcome2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keywelcome2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keywelcome2.started')
        keywelcome2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keywelcome2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keywelcome2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keywelcome2.status == STARTED and not waitOnFlip:
        theseKeys = keywelcome2.getKeys(keyList=['space'], waitRelease=False)
        _keywelcome2_allKeys.extend(theseKeys)
        if len(_keywelcome2_allKeys):
            keywelcome2.keys = _keywelcome2_allKeys[-1].name  # just the last key pressed
            keywelcome2.rt = _keywelcome2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_MessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome_Message" ---
for thisComponent in Welcome_MessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keywelcome2.keys in ['', [], None]:  # No response was made
    keywelcome2.keys = None
thisExp.addData('keywelcome2.keys',keywelcome2.keys)
if keywelcome2.keys != None:  # we had a response
    thisExp.addData('keywelcome2.rt', keywelcome2.rt)
thisExp.nextEntry()
# the Routine "Welcome_Message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Runs_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimulus_conditions_sil.xlsx'),
    seed=None, name='Runs_1')
thisExp.addLoop(Runs_1)  # add the loop to the experiment
thisRun_1 = Runs_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun_1.rgb)
if thisRun_1 != None:
    for paramName in thisRun_1:
        exec('{} = thisRun_1[paramName]'.format(paramName))

for thisRun_1 in Runs_1:
    currentLoop = Runs_1
    # abbreviate parameter names if possible (e.g. rgb = thisRun_1.rgb)
    if thisRun_1 != None:
        for paramName in thisRun_1:
            exec('{} = thisRun_1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Blocks_1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('target_highlight.xlsx'),
        seed=None, name='Blocks_1')
    thisExp.addLoop(Blocks_1)  # add the loop to the experiment
    thisBlock_1 = Blocks_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
    if thisBlock_1 != None:
        for paramName in thisBlock_1:
            exec('{} = thisBlock_1[paramName]'.format(paramName))
    
    for thisBlock_1 in Blocks_1:
        currentLoop = Blocks_1
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
        if thisBlock_1 != None:
            for paramName in thisBlock_1:
                exec('{} = thisBlock_1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_cross" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Fixation_crossComponents = [fixationcross_3, sil1_4, sil2_4, sil3_4, sil4_4, sil5_4, sil6_4]
        for thisComponent in Fixation_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_cross" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationcross_3* updates
            if fixationcross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationcross_3.frameNStart = frameN  # exact frame index
                fixationcross_3.tStart = t  # local t and not account for scr refresh
                fixationcross_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationcross_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationcross_3.started')
                fixationcross_3.setAutoDraw(True)
            if fixationcross_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationcross_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationcross_3.tStop = t  # not accounting for scr refresh
                    fixationcross_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationcross_3.stopped')
                    fixationcross_3.setAutoDraw(False)
            
            # *sil1_4* updates
            if sil1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil1_4.frameNStart = frameN  # exact frame index
                sil1_4.tStart = t  # local t and not account for scr refresh
                sil1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil1_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil1_4.started')
                sil1_4.setAutoDraw(True)
            if sil1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil1_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil1_4.tStop = t  # not accounting for scr refresh
                    sil1_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_4.stopped')
                    sil1_4.setAutoDraw(False)
            
            # *sil2_4* updates
            if sil2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil2_4.frameNStart = frameN  # exact frame index
                sil2_4.tStart = t  # local t and not account for scr refresh
                sil2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil2_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil2_4.started')
                sil2_4.setAutoDraw(True)
            if sil2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil2_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil2_4.tStop = t  # not accounting for scr refresh
                    sil2_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_4.stopped')
                    sil2_4.setAutoDraw(False)
            
            # *sil3_4* updates
            if sil3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil3_4.frameNStart = frameN  # exact frame index
                sil3_4.tStart = t  # local t and not account for scr refresh
                sil3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil3_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil3_4.started')
                sil3_4.setAutoDraw(True)
            if sil3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil3_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil3_4.tStop = t  # not accounting for scr refresh
                    sil3_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_4.stopped')
                    sil3_4.setAutoDraw(False)
            
            # *sil4_4* updates
            if sil4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil4_4.frameNStart = frameN  # exact frame index
                sil4_4.tStart = t  # local t and not account for scr refresh
                sil4_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil4_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil4_4.started')
                sil4_4.setAutoDraw(True)
            if sil4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil4_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil4_4.tStop = t  # not accounting for scr refresh
                    sil4_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_4.stopped')
                    sil4_4.setAutoDraw(False)
            
            # *sil5_4* updates
            if sil5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil5_4.frameNStart = frameN  # exact frame index
                sil5_4.tStart = t  # local t and not account for scr refresh
                sil5_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil5_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil5_4.started')
                sil5_4.setAutoDraw(True)
            if sil5_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil5_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil5_4.tStop = t  # not accounting for scr refresh
                    sil5_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_4.stopped')
                    sil5_4.setAutoDraw(False)
            
            # *sil6_4* updates
            if sil6_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil6_4.frameNStart = frameN  # exact frame index
                sil6_4.tStart = t  # local t and not account for scr refresh
                sil6_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil6_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil6_4.started')
                sil6_4.setAutoDraw(True)
            if sil6_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil6_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil6_4.tStop = t  # not accounting for scr refresh
                    sil6_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_4.stopped')
                    sil6_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_cross" ---
        for thisComponent in Fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Target_Highlight" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        highlight_.setPos(stim_location)
        highlight_.setImage(highlight)
        # keep track of which components have finished
        Target_HighlightComponents = [sil1_5, sil2_5, sil3_5, sil4_5, sil5_5, sil6_5, highlight_]
        for thisComponent in Target_HighlightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Target_Highlight" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sil1_5* updates
            if sil1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil1_5.frameNStart = frameN  # exact frame index
                sil1_5.tStart = t  # local t and not account for scr refresh
                sil1_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil1_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil1_5.started')
                sil1_5.setAutoDraw(True)
            if sil1_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil1_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil1_5.tStop = t  # not accounting for scr refresh
                    sil1_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_5.stopped')
                    sil1_5.setAutoDraw(False)
            
            # *sil2_5* updates
            if sil2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil2_5.frameNStart = frameN  # exact frame index
                sil2_5.tStart = t  # local t and not account for scr refresh
                sil2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil2_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil2_5.started')
                sil2_5.setAutoDraw(True)
            if sil2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil2_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil2_5.tStop = t  # not accounting for scr refresh
                    sil2_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_5.stopped')
                    sil2_5.setAutoDraw(False)
            
            # *sil3_5* updates
            if sil3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil3_5.frameNStart = frameN  # exact frame index
                sil3_5.tStart = t  # local t and not account for scr refresh
                sil3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil3_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil3_5.started')
                sil3_5.setAutoDraw(True)
            if sil3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil3_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil3_5.tStop = t  # not accounting for scr refresh
                    sil3_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_5.stopped')
                    sil3_5.setAutoDraw(False)
            
            # *sil4_5* updates
            if sil4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil4_5.frameNStart = frameN  # exact frame index
                sil4_5.tStart = t  # local t and not account for scr refresh
                sil4_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil4_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil4_5.started')
                sil4_5.setAutoDraw(True)
            if sil4_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil4_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil4_5.tStop = t  # not accounting for scr refresh
                    sil4_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_5.stopped')
                    sil4_5.setAutoDraw(False)
            
            # *sil5_5* updates
            if sil5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil5_5.frameNStart = frameN  # exact frame index
                sil5_5.tStart = t  # local t and not account for scr refresh
                sil5_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil5_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil5_5.started')
                sil5_5.setAutoDraw(True)
            if sil5_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil5_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil5_5.tStop = t  # not accounting for scr refresh
                    sil5_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_5.stopped')
                    sil5_5.setAutoDraw(False)
            
            # *sil6_5* updates
            if sil6_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil6_5.frameNStart = frameN  # exact frame index
                sil6_5.tStart = t  # local t and not account for scr refresh
                sil6_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil6_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil6_5.started')
                sil6_5.setAutoDraw(True)
            if sil6_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil6_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil6_5.tStop = t  # not accounting for scr refresh
                    sil6_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_5.stopped')
                    sil6_5.setAutoDraw(False)
            
            # *highlight_* updates
            if highlight_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                highlight_.frameNStart = frameN  # exact frame index
                highlight_.tStart = t  # local t and not account for scr refresh
                highlight_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(highlight_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlight_.started')
                highlight_.setAutoDraw(True)
            if highlight_.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > highlight_.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    highlight_.tStop = t  # not accounting for scr refresh
                    highlight_.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'highlight_.stopped')
                    highlight_.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Target_HighlightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Target_Highlight" ---
        for thisComponent in Target_HighlightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        Trials_1 = data.TrialHandler(nReps=5.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(conditions),
            seed=None, name='Trials_1')
        thisExp.addLoop(Trials_1)  # add the loop to the experiment
        thisTrial_1 = Trials_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
        if thisTrial_1 != None:
            for paramName in thisTrial_1:
                exec('{} = thisTrial_1[paramName]'.format(paramName))
        
        for thisTrial_1 in Trials_1:
            currentLoop = Trials_1
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
            if thisTrial_1 != None:
                for paramName in thisTrial_1:
                    exec('{} = thisTrial_1[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            stim_2.setPos(stim_loc)
            stim_2.setOri(orientation)
            stim_2.setImage(stim_trial)
            # keep track of which components have finished
            TrialComponents = [sil1_6, sil2_6, sil3_6, sil4_6, sil5_6, sil6_6, stim_2]
            for thisComponent in TrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trial" ---
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *sil1_6* updates
                if sil1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil1_6.frameNStart = frameN  # exact frame index
                    sil1_6.tStart = t  # local t and not account for scr refresh
                    sil1_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil1_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_6.started')
                    sil1_6.setAutoDraw(True)
                if sil1_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil1_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil1_6.tStop = t  # not accounting for scr refresh
                        sil1_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil1_6.stopped')
                        sil1_6.setAutoDraw(False)
                
                # *sil2_6* updates
                if sil2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil2_6.frameNStart = frameN  # exact frame index
                    sil2_6.tStart = t  # local t and not account for scr refresh
                    sil2_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil2_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_6.started')
                    sil2_6.setAutoDraw(True)
                if sil2_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil2_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil2_6.tStop = t  # not accounting for scr refresh
                        sil2_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil2_6.stopped')
                        sil2_6.setAutoDraw(False)
                
                # *sil3_6* updates
                if sil3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil3_6.frameNStart = frameN  # exact frame index
                    sil3_6.tStart = t  # local t and not account for scr refresh
                    sil3_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil3_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_6.started')
                    sil3_6.setAutoDraw(True)
                if sil3_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil3_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil3_6.tStop = t  # not accounting for scr refresh
                        sil3_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil3_6.stopped')
                        sil3_6.setAutoDraw(False)
                
                # *sil4_6* updates
                if sil4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil4_6.frameNStart = frameN  # exact frame index
                    sil4_6.tStart = t  # local t and not account for scr refresh
                    sil4_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil4_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_6.started')
                    sil4_6.setAutoDraw(True)
                if sil4_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil4_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil4_6.tStop = t  # not accounting for scr refresh
                        sil4_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil4_6.stopped')
                        sil4_6.setAutoDraw(False)
                
                # *sil5_6* updates
                if sil5_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil5_6.frameNStart = frameN  # exact frame index
                    sil5_6.tStart = t  # local t and not account for scr refresh
                    sil5_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil5_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_6.started')
                    sil5_6.setAutoDraw(True)
                if sil5_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil5_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil5_6.tStop = t  # not accounting for scr refresh
                        sil5_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil5_6.stopped')
                        sil5_6.setAutoDraw(False)
                
                # *sil6_6* updates
                if sil6_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil6_6.frameNStart = frameN  # exact frame index
                    sil6_6.tStart = t  # local t and not account for scr refresh
                    sil6_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil6_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_6.started')
                    sil6_6.setAutoDraw(True)
                if sil6_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil6_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil6_6.tStop = t  # not accounting for scr refresh
                        sil6_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil6_6.stopped')
                        sil6_6.setAutoDraw(False)
                
                # *stim_2* updates
                if stim_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_2.frameNStart = frameN  # exact frame index
                    stim_2.tStart = t  # local t and not account for scr refresh
                    stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_2.started')
                    stim_2.setAutoDraw(True)
                if stim_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_2.tStop = t  # not accounting for scr refresh
                        stim_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_2.stopped')
                        stim_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trial" ---
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed 5.0 repeats of 'Trials_1'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Blocks_1'
    
    
    # --- Prepare to start Routine "Break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    BreakComponents = [text, text_8, key_resp]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Break" ---
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Runs_1.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Runs_1.addData('key_resp.rt', key_resp.rt)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Runs_1'


# --- Prepare to start Routine "Example_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Example_endComponents = [text_7, key_resp_6]
for thisComponent in Example_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Example_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_7.started')
        text_7.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Example_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Example_end" ---
for thisComponent in Example_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Example_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Runs_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimulus_conditions_pirates.xlsx'),
    seed=None, name='Runs_2')
thisExp.addLoop(Runs_2)  # add the loop to the experiment
thisRun_2 = Runs_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun_2.rgb)
if thisRun_2 != None:
    for paramName in thisRun_2:
        exec('{} = thisRun_2[paramName]'.format(paramName))

for thisRun_2 in Runs_2:
    currentLoop = Runs_2
    # abbreviate parameter names if possible (e.g. rgb = thisRun_2.rgb)
    if thisRun_2 != None:
        for paramName in thisRun_2:
            exec('{} = thisRun_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Blocks_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('target_highlight.xlsx'),
        seed=None, name='Blocks_2')
    thisExp.addLoop(Blocks_2)  # add the loop to the experiment
    thisBlock_2 = Blocks_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
    if thisBlock_2 != None:
        for paramName in thisBlock_2:
            exec('{} = thisBlock_2[paramName]'.format(paramName))
    
    for thisBlock_2 in Blocks_2:
        currentLoop = Blocks_2
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
        if thisBlock_2 != None:
            for paramName in thisBlock_2:
                exec('{} = thisBlock_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation_cross" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Fixation_crossComponents = [fixationcross_3, sil1_4, sil2_4, sil3_4, sil4_4, sil5_4, sil6_4]
        for thisComponent in Fixation_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation_cross" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationcross_3* updates
            if fixationcross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationcross_3.frameNStart = frameN  # exact frame index
                fixationcross_3.tStart = t  # local t and not account for scr refresh
                fixationcross_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationcross_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationcross_3.started')
                fixationcross_3.setAutoDraw(True)
            if fixationcross_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationcross_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationcross_3.tStop = t  # not accounting for scr refresh
                    fixationcross_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationcross_3.stopped')
                    fixationcross_3.setAutoDraw(False)
            
            # *sil1_4* updates
            if sil1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil1_4.frameNStart = frameN  # exact frame index
                sil1_4.tStart = t  # local t and not account for scr refresh
                sil1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil1_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil1_4.started')
                sil1_4.setAutoDraw(True)
            if sil1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil1_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil1_4.tStop = t  # not accounting for scr refresh
                    sil1_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_4.stopped')
                    sil1_4.setAutoDraw(False)
            
            # *sil2_4* updates
            if sil2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil2_4.frameNStart = frameN  # exact frame index
                sil2_4.tStart = t  # local t and not account for scr refresh
                sil2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil2_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil2_4.started')
                sil2_4.setAutoDraw(True)
            if sil2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil2_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil2_4.tStop = t  # not accounting for scr refresh
                    sil2_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_4.stopped')
                    sil2_4.setAutoDraw(False)
            
            # *sil3_4* updates
            if sil3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil3_4.frameNStart = frameN  # exact frame index
                sil3_4.tStart = t  # local t and not account for scr refresh
                sil3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil3_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil3_4.started')
                sil3_4.setAutoDraw(True)
            if sil3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil3_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil3_4.tStop = t  # not accounting for scr refresh
                    sil3_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_4.stopped')
                    sil3_4.setAutoDraw(False)
            
            # *sil4_4* updates
            if sil4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil4_4.frameNStart = frameN  # exact frame index
                sil4_4.tStart = t  # local t and not account for scr refresh
                sil4_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil4_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil4_4.started')
                sil4_4.setAutoDraw(True)
            if sil4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil4_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil4_4.tStop = t  # not accounting for scr refresh
                    sil4_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_4.stopped')
                    sil4_4.setAutoDraw(False)
            
            # *sil5_4* updates
            if sil5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil5_4.frameNStart = frameN  # exact frame index
                sil5_4.tStart = t  # local t and not account for scr refresh
                sil5_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil5_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil5_4.started')
                sil5_4.setAutoDraw(True)
            if sil5_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil5_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil5_4.tStop = t  # not accounting for scr refresh
                    sil5_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_4.stopped')
                    sil5_4.setAutoDraw(False)
            
            # *sil6_4* updates
            if sil6_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil6_4.frameNStart = frameN  # exact frame index
                sil6_4.tStart = t  # local t and not account for scr refresh
                sil6_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil6_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil6_4.started')
                sil6_4.setAutoDraw(True)
            if sil6_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil6_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil6_4.tStop = t  # not accounting for scr refresh
                    sil6_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_4.stopped')
                    sil6_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation_cross" ---
        for thisComponent in Fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Target_Highlight" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        highlight_.setPos(stim_location)
        highlight_.setImage(highlight)
        # keep track of which components have finished
        Target_HighlightComponents = [sil1_5, sil2_5, sil3_5, sil4_5, sil5_5, sil6_5, highlight_]
        for thisComponent in Target_HighlightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Target_Highlight" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sil1_5* updates
            if sil1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil1_5.frameNStart = frameN  # exact frame index
                sil1_5.tStart = t  # local t and not account for scr refresh
                sil1_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil1_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil1_5.started')
                sil1_5.setAutoDraw(True)
            if sil1_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil1_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil1_5.tStop = t  # not accounting for scr refresh
                    sil1_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_5.stopped')
                    sil1_5.setAutoDraw(False)
            
            # *sil2_5* updates
            if sil2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil2_5.frameNStart = frameN  # exact frame index
                sil2_5.tStart = t  # local t and not account for scr refresh
                sil2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil2_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil2_5.started')
                sil2_5.setAutoDraw(True)
            if sil2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil2_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil2_5.tStop = t  # not accounting for scr refresh
                    sil2_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_5.stopped')
                    sil2_5.setAutoDraw(False)
            
            # *sil3_5* updates
            if sil3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil3_5.frameNStart = frameN  # exact frame index
                sil3_5.tStart = t  # local t and not account for scr refresh
                sil3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil3_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil3_5.started')
                sil3_5.setAutoDraw(True)
            if sil3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil3_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil3_5.tStop = t  # not accounting for scr refresh
                    sil3_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_5.stopped')
                    sil3_5.setAutoDraw(False)
            
            # *sil4_5* updates
            if sil4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil4_5.frameNStart = frameN  # exact frame index
                sil4_5.tStart = t  # local t and not account for scr refresh
                sil4_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil4_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil4_5.started')
                sil4_5.setAutoDraw(True)
            if sil4_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil4_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil4_5.tStop = t  # not accounting for scr refresh
                    sil4_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_5.stopped')
                    sil4_5.setAutoDraw(False)
            
            # *sil5_5* updates
            if sil5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil5_5.frameNStart = frameN  # exact frame index
                sil5_5.tStart = t  # local t and not account for scr refresh
                sil5_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil5_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil5_5.started')
                sil5_5.setAutoDraw(True)
            if sil5_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil5_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil5_5.tStop = t  # not accounting for scr refresh
                    sil5_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_5.stopped')
                    sil5_5.setAutoDraw(False)
            
            # *sil6_5* updates
            if sil6_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sil6_5.frameNStart = frameN  # exact frame index
                sil6_5.tStart = t  # local t and not account for scr refresh
                sil6_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sil6_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sil6_5.started')
                sil6_5.setAutoDraw(True)
            if sil6_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sil6_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sil6_5.tStop = t  # not accounting for scr refresh
                    sil6_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_5.stopped')
                    sil6_5.setAutoDraw(False)
            
            # *highlight_* updates
            if highlight_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                highlight_.frameNStart = frameN  # exact frame index
                highlight_.tStart = t  # local t and not account for scr refresh
                highlight_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(highlight_, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlight_.started')
                highlight_.setAutoDraw(True)
            if highlight_.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > highlight_.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    highlight_.tStop = t  # not accounting for scr refresh
                    highlight_.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'highlight_.stopped')
                    highlight_.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Target_HighlightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Target_Highlight" ---
        for thisComponent in Target_HighlightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        Trials_2 = data.TrialHandler(nReps=5.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(conditions),
            seed=None, name='Trials_2')
        thisExp.addLoop(Trials_2)  # add the loop to the experiment
        thisTrial_2 = Trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in Trials_2:
            currentLoop = Trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            stim_2.setPos(stim_loc)
            stim_2.setOri(orientation)
            stim_2.setImage(stim_trial)
            # keep track of which components have finished
            TrialComponents = [sil1_6, sil2_6, sil3_6, sil4_6, sil5_6, sil6_6, stim_2]
            for thisComponent in TrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trial" ---
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *sil1_6* updates
                if sil1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil1_6.frameNStart = frameN  # exact frame index
                    sil1_6.tStart = t  # local t and not account for scr refresh
                    sil1_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil1_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil1_6.started')
                    sil1_6.setAutoDraw(True)
                if sil1_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil1_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil1_6.tStop = t  # not accounting for scr refresh
                        sil1_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil1_6.stopped')
                        sil1_6.setAutoDraw(False)
                
                # *sil2_6* updates
                if sil2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil2_6.frameNStart = frameN  # exact frame index
                    sil2_6.tStart = t  # local t and not account for scr refresh
                    sil2_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil2_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil2_6.started')
                    sil2_6.setAutoDraw(True)
                if sil2_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil2_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil2_6.tStop = t  # not accounting for scr refresh
                        sil2_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil2_6.stopped')
                        sil2_6.setAutoDraw(False)
                
                # *sil3_6* updates
                if sil3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil3_6.frameNStart = frameN  # exact frame index
                    sil3_6.tStart = t  # local t and not account for scr refresh
                    sil3_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil3_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil3_6.started')
                    sil3_6.setAutoDraw(True)
                if sil3_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil3_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil3_6.tStop = t  # not accounting for scr refresh
                        sil3_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil3_6.stopped')
                        sil3_6.setAutoDraw(False)
                
                # *sil4_6* updates
                if sil4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil4_6.frameNStart = frameN  # exact frame index
                    sil4_6.tStart = t  # local t and not account for scr refresh
                    sil4_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil4_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil4_6.started')
                    sil4_6.setAutoDraw(True)
                if sil4_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil4_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil4_6.tStop = t  # not accounting for scr refresh
                        sil4_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil4_6.stopped')
                        sil4_6.setAutoDraw(False)
                
                # *sil5_6* updates
                if sil5_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil5_6.frameNStart = frameN  # exact frame index
                    sil5_6.tStart = t  # local t and not account for scr refresh
                    sil5_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil5_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil5_6.started')
                    sil5_6.setAutoDraw(True)
                if sil5_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil5_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil5_6.tStop = t  # not accounting for scr refresh
                        sil5_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil5_6.stopped')
                        sil5_6.setAutoDraw(False)
                
                # *sil6_6* updates
                if sil6_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sil6_6.frameNStart = frameN  # exact frame index
                    sil6_6.tStart = t  # local t and not account for scr refresh
                    sil6_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sil6_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sil6_6.started')
                    sil6_6.setAutoDraw(True)
                if sil6_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sil6_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        sil6_6.tStop = t  # not accounting for scr refresh
                        sil6_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sil6_6.stopped')
                        sil6_6.setAutoDraw(False)
                
                # *stim_2* updates
                if stim_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_2.frameNStart = frameN  # exact frame index
                    stim_2.tStart = t  # local t and not account for scr refresh
                    stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_2.started')
                    stim_2.setAutoDraw(True)
                if stim_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_2.tStop = t  # not accounting for scr refresh
                        stim_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_2.stopped')
                        stim_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trial" ---
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
        # completed 5.0 repeats of 'Trials_2'
        
    # completed 1.0 repeats of 'Blocks_2'
    
    
    # --- Prepare to start Routine "Break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    BreakComponents = [text, text_8, key_resp]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Break" ---
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Runs_2.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Runs_2.addData('key_resp.rt', key_resp.rt)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'Runs_2'


# --- Prepare to start Routine "Finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
FinishComponents = [text_9, key_resp_5]
for thisComponent in FinishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_9.started')
        text_9.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Finish" ---
for thisComponent in FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
