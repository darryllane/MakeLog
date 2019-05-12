import unittest
import warnings
from MakeLog import make_log as log
import os 

class TestMakeLog(unittest.TestCase):
		
	def read(self, filename):
		if not os.path.exists(filename):
			print('The file does not exist: {}'.format(filename))
			sys.exit()
		else:
			data = [line.rstrip('\n') for line in open(filename)]
			return data
	
	def checkout(self, data):
		if isinstance(data, list):
			if 'debug' in data[0]:
				return True
			elif 'info' in data[0]:
				return True
			elif 'error' in data[0]:
				return True
		else:
			return False	
	
	def test_error(self):
		print('\nTesting error log write\n')
		logger = log.initialise()
		logger.error('error_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.error = self.read(logger.ERROR_LOG_FILE)
			successful = self.checkout(self.error)
			self.assertTrue(successful, True)

	def test_info(self):
		print('\nTesting info log write\n')
		logger = log.initialise()
		logger.info('info_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.info = self.read(logger.INFO_LOG_FILE)		
			successful = self.checkout(self.info)
			self.assertTrue(successful, True)

	def test_debug(self):
		print('\nTesting debug log write\n')
		logger = log.initialise()
		logger.debug('debug_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.debug = self.read(logger.DEBUG_LOG_FILE)
			successful = self.checkout(self.debug)
			self.assertTrue(successful, True)

if __name__ == '__main__':
	unittest.main()