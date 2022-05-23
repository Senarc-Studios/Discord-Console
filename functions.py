import json

from typing import Any

class Constants:
    def __init__(self):
        file_ = open('config.json')
        self.constants = json.load(file_)

    @classmethod
    def get(self, constant: str) -> Any:
        return self.constants[constant]