#!/usr/bin/env python
import logging
import time
from daemon import runner

# Daemon and main
# Will Blew was here :P

class Autode():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path == '/var/run/Autode/Autode.pid'
		self.pidfile_timeout = 10

	def run(self):
		white True:
			# Do all of the things, well kind of. We'll be sure to modulize an such

			# Please to be logging
			logger.debug("DEBUG: ")
			logger.info("INFO: ")
			logger.warn("WARNING: ")
			logger.error("ERROR: ")
			time.sleep(5)
autode = Autode()
log = logging.getLogger("AutodeLog")
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s -- %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/Autode/Autode.log")
handler.setFormatter(format)
log.addHandler(handler)

daemoner = runner.DaemonRunner(autode)
daemoner.daemon_context.files_preserve=[handler.stream]
daemoner.do_action()