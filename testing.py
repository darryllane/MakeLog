from make_log import initialise

logger = initialise()

print('Log Directory: {}'.format(logger.LOG_DIR))

logger.info('test')
logger.error('test')
logger.debug('test')
print('info, error and debug logs created')