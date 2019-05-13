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
	
	def test_error_default(self):
		print('\n\nTesting default error log write')
		logger = log.initialise()
		logger.error('error_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.error = self.read(logger.ERROR_LOG_FILE)
			successful = self.checkout(self.error)
			self.assertTrue(successful, True)

	def test_info_default(self):
		print('\n\nTesting default info log write')
		logger = log.initialise()
		logger.info('info_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.info = self.read(logger.INFO_LOG_FILE)		
			successful = self.checkout(self.info)
			self.assertTrue(successful, True)

	def test_debug_default(self):
		print('\n\nTesting default debug log write')
		logger = log.initialise()
		logger.debug('debug_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.debug = self.read(logger.DEBUG_LOG_FILE)
			successful = self.checkout(self.debug)
			self.assertTrue(successful, True)
			

	def test_error_custom(self):
		print('\n\nTesting custom error log write')
		logger = log.initialise(LOG_DIR='~/custom_log/', ERROR_LOG_FILE = 'error_log.log')
		logger.error('error_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.error = self.read(logger.ERROR_LOG_FILE)
			successful = self.checkout(self.error)
			self.assertTrue(successful, True)

	def test_info_custom(self):
		print('\n\nTesting custom info log write')
		logger = log.initialise(LOG_DIR='~/custom_log/', INFO_LOG_FILE = 'information_log.log')
		logger.info('info_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.info = self.read(logger.INFO_LOG_FILE)		
			successful = self.checkout(self.info)
			self.assertTrue(successful, True)

	def test_debug_custom(self):
		print('\n\nTesting custom debug log write')
		logger = log.initialise(LOG_DIR='~/custom_log/', DEBUG_LOG_FILE = 'debug_log.log')
		logger.debug('debug_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.debug = self.read(logger.DEBUG_LOG_FILE)
			successful = self.checkout(self.debug)
			self.assertTrue(successful, True)
			
	
	def test_error_custom2(self):
		print('\n\nTesting custom error log with prefixed /')
		logger = log.initialise(LOG_DIR='~/custom_log/', ERROR_LOG_FILE = '/error_log2.log')
		logger.error('error_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.error = self.read(logger.ERROR_LOG_FILE)
			successful = self.checkout(self.error)
			self.assertTrue(successful, True)

	def test_info_custom2(self):
		print('\n\nTesting custom info log with prefixed /')
		logger = log.initialise(LOG_DIR='~/custom_log/', INFO_LOG_FILE = '/information_log2.log')
		logger.info('info_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.info = self.read(logger.INFO_LOG_FILE)		
			successful = self.checkout(self.info)
			self.assertTrue(successful, True)

	def test_debug_custom2(self):
		print('\n\nTesting custom debug log with prefixed /')
		logger = log.initialise(LOG_DIR='~/custom_log/', DEBUG_LOG_FILE = '/debug_log2.log')
		logger.debug('debug_test')
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")		
			self.debug = self.read(logger.DEBUG_LOG_FILE)
			successful = self.checkout(self.debug)
			self.assertTrue(successful, True)			
			

if __name__ == '__main__':
	unittest.main()