#!/usr/bin/env python
import psutil

def cpuInfo():
	cpu_percent = psutil.cpu_percent(interval=1)
	return cpu_percent
