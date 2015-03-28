#!/usr/bin/env python
import cpu
import logger
import api

def doChecks():
	#check cpu
	if cpuCap != 0: 
		cpuPercent = cpu.cpuInfo
		if cpuPercent < cpuCap: # If we're good then ignore
			return false
		else:
			startTimer(time) #Not yet implemented calls a tick to check for clone complete for scaling.
			return true
	#check io

	#check bandwidth

def cloneLinode():


def swapIp():

def createImage():

def triggerJson():