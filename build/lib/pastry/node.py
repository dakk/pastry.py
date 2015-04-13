from threading import Thread
from threading import Lock
from colorlog import ColoredFormatter
import logging


formatter = ColoredFormatter(
	'%(log_color)s[%(asctime)-8s] %(module)s (%(process)d %(threadName)s): %(message_log_color)s%(message)s',
	datefmt=None,
	reset=True,
	log_colors={
		'DEBUG':    'blue',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red',
	},
	secondary_log_colors={
		'message': {
			'DEBUG':    'purple',
			'INFO':     'yellow',
			'WARNING':  'green',
			'ERROR':    'yellow',
			'CRITICAL': 'red',
		}
	},
	style = '%'
)

stream = logging.StreamHandler()
stream.setFormatter(formatter)

logger = logging.getLogger('pastry.py')
logger.addHandler(stream)
logger.setLevel (logging.DEBUG)


class Node:
	def __init__ (self, port, auth):
		self.port = port
		self.auth = auth
		logger.debug ('listening on port %d', self.port)

	def bootstrap (self, seeds = []):
		for seed in seeds:
			logger.debug ('bootstraping from %s', str (seed))

	def get (self, key):
		pass

	def set (self, key, data):
		pass


	
	
