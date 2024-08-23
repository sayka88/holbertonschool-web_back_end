#!/usr/bin/env python3
"""Write a Python function that inserts a new document
in a collection based on kwargs:"""


def insert_school(mongo_collection, **kwargs):
    """Write a Python function that inserts a new document
    in a collection based on kwargs:"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
