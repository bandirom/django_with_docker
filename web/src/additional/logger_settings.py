import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'warning': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'log.log',
            'formatter': 'warning',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'app': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,  # дає можливість іншим логерам обробити лог - наприклад root
        }
    },
}
