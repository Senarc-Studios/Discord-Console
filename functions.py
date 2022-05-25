import json

from typing import Any

file_ = open('config.json')
constants = json.load(file_)
class Constants:
    @staticmethod
    def get(constant: str) -> Any:
        return constants[constant]