from inventory_report.importer.importer import Importer
from pathlib import Path
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        file_extension = Path(path).suffix
        if file_extension != ".json":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return json.load(file)
