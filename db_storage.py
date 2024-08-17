#!/usr/bin/env python3
"""Module: db_storage
Defines the class that implement the database storage engine
"""
from models import Task


class DBStorage:
    """Defines database storage engine"""

    def __init__(self, db):
        """initialize engine"""
        self.db = db

    def save(self, task):
        """save task to the todos table of the database"""
        self.db.session.add(task)
        self.db.session.commit()
