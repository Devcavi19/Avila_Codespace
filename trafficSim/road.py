import random
import time
import threading
import pygame
import sys

# Default values of signal timers in seconds
defaultGreen = {0:20, 1:20, 2:20, 3:20}
defaultRed = 150
defaultYellow = 5
signals = []
noOfSignals = 4
currentGreen = 0   # Indicates which signal is green currently
nextGreen = (currentGreen+1)%noOfSignals 
currentYellow = 0   # Indicates whether yellow signal is on or off
speeds = {'car':2.25, 'bus':1.8, 'truck':1.8, 'bike':2.5}  # average speeds of vehicles

# Coordinates of vehicles’ start
x = {'right':[0,0,0], 'down':[0,745,710], 'left':[1400,1400,1400], 'up':[800,627,657]}
y = {'right':[0,365,335], 'down':[0,0,0], 'left':[1400,448,420], 'up':[800,800,800]}

vehicles = {'right': {0:[], 1:[], 2:[], 'crossed':0}, 'down': {0:[], 1:[], 2:[], 'crossed':0}, 'left': {0:[], 1:[], 2:[], 'crossed':0}, 'up': {0:[], 1:[], 2:[], 'crossed':0}}
vehicleTypes = {0:'car', 1:'bus', 2:'truck', 3:'bike'}
directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'}
# Coordinates of signal image, timer, and vehicle count
signalCoods = [(585,230),(781,230),(781,500),(585,500)]
signalTimerCoods = [(585,210),(781,210),(781,482),(585,482)]
# Coordinates of stop lines
stopLines = {'right': 590, 'down': 330, 'left': 760, 'up': 460}
defaultStop = {'right': 580, 'down': 320, 'left': 780, 'up': 480}
# Gap between vehicles
stoppingGap = 15    # stopping gap
movingGap = 15   # moving gap

pygame.init()
simulation = pygame.sprite.Group()

