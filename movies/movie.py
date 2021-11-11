from enum import Enum
import json


class Movie:
    def __init__(self, thumb, title):
        self.thumb = thumb
        self.title = title

    def to_dict(self):
        return {"thumb": self.thumb, "title": self.title }