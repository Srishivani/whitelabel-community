# DB package initialization
from .base import Database
from .mongodb import MongoDatabase

__all__ = ['Database', 'MongoDatabase']
