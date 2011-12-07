from __future__ import absolute_import
from .base import *

from bundle_config import config

REDIS_HOST = config['redis']['host']
REDIS_PORT = int(config['redis']['port'])
REDIS_PASSWORD = config['redis']['password']
REDIS_DB = 0

MEDIA_ROOT = config['core']['data_directory']
