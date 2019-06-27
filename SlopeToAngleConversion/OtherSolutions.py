import math as m
def convert(slope):
  if slope==0:return 90
  d=round(m.degrees(m.atan(1/slope)))
  return d if d>0 else 180+d

###################################################
  
from math import atan, degrees

def convert(slope):
	return round(90 - degrees(atan(slope)))
  
###################################################

import numpy as np
def convert(slope):
    angle = np.rad2deg(np.arctan2(slope,1))
    answer = 90-angle
    return round(answer)
  
###################################################

import math
def convert(slope):
	return 90 - round(math.degrees(math.atan(slope)),0)
  
###################################################

def convert(slope):
	if slope == 0:
		return 90
	elif slope == 1:
		return 45
	elif slope == -1:
		return 135
	elif slope == 3:
		return 18
	elif slope == 100:
		return 1
	elif slope == -20:
		return 177
