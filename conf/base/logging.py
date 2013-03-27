LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'logs/django.log', # FIXME(andrew)
            'maxBytes': 1024*1024*50,
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
		# FIXME(andrew)
                'filename': 'logs/django_request.log',
                'maxBytes': 1024*1024*5,
                'backupCount': 5,
                'formatter':'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


