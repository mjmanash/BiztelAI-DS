import json

class ChatProcessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)
