#!/usr/bin/env python3
"""Write a Python function that returns all students sorted by average score:

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore"""
from typing import List
from pymongo import collection


def top_students(mongo_collection) -> List[dict]:
    """function that returns all students sorted by average score"""
    return list(mongo_collection.aggregate([
        {
            '$addFields': {
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }

    ]))
