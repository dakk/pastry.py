from threading import Thread
from threading import Lock
import logging

logging.basicConfig(format='[%(asctime)-8s] %(module)s - %(message)s', level=logging.DEBUG)

class Node:
	def __init__ (self, port, auth):
		logging.debug ('Node initialized')

	def bootstrap (self, seeds = []):
		pass

	def get (self, key):
		pass

	def set (self, key, data):
		pass


	
	
