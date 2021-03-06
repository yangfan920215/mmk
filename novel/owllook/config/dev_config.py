#!/usr/bin/env python
import os

from .config import Config


class DevConfig(Config):
    """eix
    Dev config for owllook
    """

    # Database config
    REDIS_DICT = dict(
        IS_CACHE=True,
        REDIS_ENDPOINT=os.getenv('REDIS_ENDPOINT', "localhost"),
        REDIS_PORT=os.getenv('REDIS_PORT', 6379),
        REDIS_PASSWORD=os.getenv('REDIS_PASSWORD', None),
        CACHE_DB=0,
        SESSION_DB=1,
        POOLSIZE=10,
    )
    MONGODB = dict(
        MONGO_HOST=os.getenv('MONGO_HOST', ""),
        MONGO_PORT=os.getenv('MONGO_PORT', 27017),
        MONGO_USERNAME=os.getenv('MONGO_USERNAME', ""),
        MONGO_PASSWORD=os.getenv('MONGO_PASSWORD', ""),
        DATABASE='owllook',
    )
