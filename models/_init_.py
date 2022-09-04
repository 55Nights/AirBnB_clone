#!/usr/bin/python3
"""__init__ magic method for models directory"""
from errno import WSAEDQUOT
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
:WSAEDQUOT