import os
import json

class JsonWriter:
    def __init__(self):
        self.base_dir = os.path.dirname(__file__)  # json_output kaust
        os.makedirs(self.base_dir, exist_ok=True)

    def write(self, filename, data):
        file_path = os.path.join(self.base_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
