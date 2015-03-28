#!/usr/bin/env python
import logging
import time
import sys
from daemon import runner
sys.path.append('mods')
import cpu
import confData

# Daemon and main
# Will Blew was here :P

class Autode():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path = '/var/run/Autode/Autode.pid'
		self.pidfile_timeout = 10

	def run(self):
		while True:
			# Do all of the things, well kind of. We'll be sure to modulize an such

			#call action first for all checks
			timeEnd = time.time() + 60 * 15
			while time.time() < t_end:
				action.doChecks()

			# Please to be logging, we're going to strip this out in favor of a modulized logger.
			log.debug("DEBUG: ")
			log.info("INFO: ")
			log.warn("WARNING: ")
			log.error("ERROR: ")
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